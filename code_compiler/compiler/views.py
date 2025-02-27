from django.shortcuts import render
import subprocess
import os
import json
import uuid  # 🔹 To generate unique filenames
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CodeSubmission, ErrorLog
from .error_suggestions import get_ai_suggestions  # Ensure correct import

@csrf_exempt
def execute_code(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            language = data.get("language", "").strip().lower()
            code = data.get("code", "")
            user_input = data.get("user_input", "")

            if not code:
                return JsonResponse({"error": "No code provided"}, status=400)

            temp_filename = f"temp_{uuid.uuid4().hex[:8]}"
            extension = ""

            if language == "python":
                extension = ".py"
                command = f"python3 {temp_filename + extension}"
            elif language == "java":
                extension = ".java"
                temp_filename = "Main"
                compile_command = f"javac {temp_filename + extension}"
                run_command = f"java {temp_filename}"
            elif language == "c":
                extension = ".c"
                compile_command = f"gcc {temp_filename + extension} -o {temp_filename}"
                run_command = f"./{temp_filename}"
            else:
                return JsonResponse({"error": "Unsupported language"}, status=400)

            # Write user code to a temporary file
            with open(temp_filename + extension, "w") as temp_file:
                temp_file.write(code)

            try:
                if language == "java":
                    compile_result = subprocess.run(compile_command, shell=True, capture_output=True, text=True)
                    if compile_result.returncode != 0:
                        output = compile_result.stderr
                    else:
                        result = subprocess.run(run_command, shell=True, capture_output=True, text=True, input=user_input, timeout=5)
                        output = result.stdout if result.returncode == 0 else result.stderr
                elif language == "c":
                    compile_result = subprocess.run(compile_command, shell=True, capture_output=True, text=True)
                    if compile_result.returncode != 0:
                        output = compile_result.stderr
                    else:
                        result = subprocess.run(run_command, shell=True, capture_output=True, text=True, input=user_input, timeout=5)
                        output = result.stdout if result.returncode == 0 else result.stderr
                else:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, input=user_input, timeout=5)
                    output = result.stdout if result.returncode == 0 else result.stderr

            except Exception as e:
                output = str(e)

            # Clean up temporary files
            try:
                os.remove(temp_filename + extension)
                if language == "java":
                    os.remove(temp_filename + ".class")
                if language == "c":
                    os.remove(temp_filename)
            except FileNotFoundError:
                pass

            # Save to database
            submission = CodeSubmission.objects.create(language=language, code=code, output=output)

            return JsonResponse({"output": output, "submission_id": submission.id})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "GET method not allowed. Use POST."}, status=405)



def error_suggestions(request, submission_id):
    try:
        submission = CodeSubmission.objects.get(id=submission_id)
    except CodeSubmission.DoesNotExist:
        return JsonResponse({"error": "Invalid submission ID"}, status=404)

    if submission.output:  # Assuming output contains the error message
        suggestion = get_ai_suggestions(submission.code, submission.output)  
        error_log, created = ErrorLog.objects.get_or_create(submission=submission, defaults={'ai_suggestion': suggestion})
        
        if not created:  # If entry already exists, update it
            error_log.ai_suggestion = suggestion
            error_log.save()
        
        return JsonResponse({"suggestion": suggestion})
    
    return JsonResponse({"error": "No error found in the submission"})


def home(request):
    return render(request, "compiler/home.html")
