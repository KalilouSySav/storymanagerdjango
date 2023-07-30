from django.core import serializers
from django.core.serializers import json
from django.shortcuts import get_object_or_404, HttpResponse, JsonResponse
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods

from .models import Project, Character, Scenario
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404, HttpResponse
import json
from django.shortcuts import HttpResponse, JsonResponse
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def create_project(request):
    if request.method == 'POST':
        data = request.POST
        # Assuming 'title' and 'description' are required fields for a project
        title = data.get('title')
        description = data.get('description')

        if title and description:
            project = Project.objects.create(title=title, description=description)
            return HttpResponse(project.id)
        else:
            return HttpResponse("Error: Title and description are required fields.", status=400)
    else:
        return HttpResponse("GET request received for creating a project. Use a form to submit the data.")
def get_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return JsonResponse({'id': project.id, 'title': project.title, 'description': project.description})

def get_all_projects(request):
    # Implement get_all_projects() method
    projects = Project.objects.all()
    projects_json = serializers.serialize('json', projects)
    return HttpResponse(projects_json, content_type='application/json')
@csrf_exempt
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        description = data.get('description')

        if title and description:
            project.title = title
            project.description = description
            project.save()
            return JsonResponse({'status': 'success', 'message': 'Project updated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Title and description are required fields.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for updating the project.'}, status=405)
@csrf_exempt
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'DELETE':
        project.delete()
        return JsonResponse({'status': 'success', 'message': 'Project deleted successfully!'})

@csrf_exempt
def create_character(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        attributes = data.get('attributes')  # Assuming you pass JSON-encoded data for attributes field
        description = data.get('description')
        background = data.get('background')

        if name and description:
            character = Character.objects.create(name=name, attributes=attributes,
                                                 description=description, background=background, project=project)
            return JsonResponse({'status': 'success', 'message': 'Character created successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Name and description are required fields.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for creating a character.'}, status=405)
def get_character(request, project_id, character_id):
    character = get_object_or_404(Character, id=character_id, project_id=project_id)
    return JsonResponse({'id': character.id, 'name': character.name, 'attributes': character.attributes,
                         'description': character.description, 'background': character.background})
def get_all_characters(request, project_id):
    characters = Character.objects.filter(project_id=project_id)
    characters_json = serializers.serialize('json', characters)
    return HttpResponse(characters_json, content_type='application/json')

@csrf_exempt
def update_character(request, project_id, character_id):
    character = get_object_or_404(Character, id=character_id, project_id=project_id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        attributes = data.get('attributes')
        description = data.get('description')
        background = data.get('background')

        if name and description:
            character.name = name
            character.attributes = attributes
            character.description = description
            character.background = background
            character.save()
            return JsonResponse({'status': 'success', 'message': 'Character updated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Name and description are required fields.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for updating a character.'}, status=405)
@csrf_exempt
def delete_character(request, project_id, character_id):
    character = get_object_or_404(Character, id=character_id, project_id=project_id)

    if request.method == 'DELETE':
        character.delete()
        return JsonResponse({'status': 'success', 'message': 'Character deleted successfully!'})
@csrf_exempt
def create_scenario(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')

        if name and description:
            scenario = Scenario.objects.create(name=name, description=description, project=project)
            return JsonResponse({'status': 'success', 'message': 'Scenario created successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Name and description are required fields.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for creating a scenario.'}, status=405)
def get_scenario(request, project_id, scenario_id):
    scenario = get_object_or_404(Scenario, id=scenario_id, project_id=project_id)
    return JsonResponse({'id': scenario.id, 'name': scenario.name, 'description': scenario.description})
def get_all_scenarios(request, project_id):
    scenarios = Scenario.objects.filter(project_id=project_id)
    scenarios_json = serializers.serialize('json', scenarios)
    return HttpResponse(scenarios_json, content_type='application/json')
@csrf_exempt
def update_scenario(request, project_id, scenario_id):
    scenario = get_object_or_404(Scenario, id=scenario_id, project_id=project_id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')

        if name and description:
            scenario.name = name
            scenario.description = description
            scenario.save()
            return JsonResponse({'status': 'success', 'message': 'Scenario updated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Name and description are required fields.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for updating a scenario.'}, status=405)
@csrf_exempt
def delete_scenario(request, project_id, scenario_id):
    scenario = get_object_or_404(Scenario, id=scenario_id, project_id=project_id)

    if request.method == 'DELETE':
        scenario.delete()
        return JsonResponse({'status': 'success', 'message': 'Scenario deleted successfully!'})
def export_project(request, project_id, format):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'GET':
        if format == 'pdf':
            # # Create a PDF file
            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = f'attachment; filename="{project.title}.pdf"'
            #
            # # Create a canvas to draw on the PDF
            # buffer = io.BytesIO()
            # c = canvas.Canvas(buffer, pagesize=letter)
            #
            # # Draw the project data on the PDF
            # c.drawString(100, 800, f"Project Title: {project.title}")
            # c.drawString(100, 780, f"Description: {project.description}")
            #
            # # You can add more details and customize the layout based on your requirements
            #
            # # Save the canvas to the response and close it
            # c.save()
            # pdf = buffer.getvalue()
            # buffer.close()
            # response.write(pdf)
            #
            # return response
            return HttpResponse("Export to PDF format is not implemented yet.", status=501)

        elif format == 'word':
            # Export the project data as a Word document
            # Implement the logic to generate the Word document here

            # For example, you can use the python-docx library to create a Word document
            # and add the project data as paragraphs or tables to the document

            # Once you have the Word document content, you can return it as a response
            # For example:
            # response = HttpResponse(content_type='application/msword')
            # response['Content-Disposition'] = f'attachment; filename="{project.title}.docx"'
            # response.write(your_word_document_content_here)

            # return response

            return HttpResponse("Export to Word format is not implemented yet.", status=501)

        else:
            return HttpResponse("Invalid export format.", status=400)

    return HttpResponse("Invalid request method.", status=405)

def import_project(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if not file:
            return JsonResponse({'status': 'error', 'message': 'No file provided.'}, status=400)

        try:
            data = json.loads(file.read())
            # Assuming the JSON data contains information for projects, characters, and scenarios
            # You can iterate through the JSON data and create corresponding objects

            if 'projects' in data:
                for project_data in data['projects']:
                    title = project_data.get('title')
                    description = project_data.get('description')
                    # Create a new Project object using the provided data
                    Project.objects.create(title=title, description=description)
                    # ...

            if 'characters' in data:
                for character_data in data['characters']:
                    name = character_data.get('name')
                    description = character_data.get('description')
                    project_id = character_data.get('project_id')
                    # Get the project corresponding to project_id
                    project = Project.objects.get(id=project_id)
                    # Create a new Character object related to the project
                    Character.objects.create(project=project, name=name, description=description)
                    # ...

            if 'scenarios' in data:
                for scenario_data in data['scenarios']:
                    name = scenario_data.get('name')
                    description = scenario_data.get('description')
                    project_id = scenario_data.get('project_id')
                    # Get the project corresponding to project_id
                    project = Project.objects.get(id=project_id)
                    # Create a new Scenario object related to the project
                    Scenario.objects.create(project=project, name=name, description=description)
                    # ...

            return JsonResponse({'status': 'success', 'message': 'Project imported successfully!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data in the file.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
