from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import Detailform
from .models import Details
from .ai_service import generate_remarks
import markdown
import bleach

# Create your views here.
# def  index(request):
#     return render (request,"create.html")
    # return HttpResponse("HI")

def creates(request):
    if request.method == "POST":
        form = Detailform(request.POST)

        if form.is_valid():
            patient = form.save(commit=False)

            try:
                patient.remarks = generate_remarks(
                    patient.glucose,
                    patient.haemoglobin,
                    patient.cholesterol
                )

            except Exception as e:
                print("Gemini API Error:", e)
                patient.remarks = "AI service temporarily unavailable."

            patient.save()

            return redirect('index')

    else:
        form = Detailform()

    return render(request, 'create.html', {'form': form})

# def index(request):
#     data = Details.objects.all()

#     return render(request, 'index.html', {'data': data})
def index(request):
    data = Details.objects.all()

    for patient in data:
        html = markdown.markdown(patient.remarks or "")

        patient.formatted_remarks = bleach.clean(
            html,
            tags=[
                "h3", "p", "ul", "ol", "li",
                "strong", "em", "br"
            ],
            strip=True
        )

    return render(request, 'index.html', {'data': data})

def update(request, id):
    obj = get_object_or_404(Details, id=id)

    if request.method == "POST":
        form = Detailform(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = Detailform(instance=obj)

    return render(request, 'update.html', {'form': form})

def delete(request, id):
    obj = get_object_or_404(Details, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect('index')

    return render(request, 'delete.html', {'obj': obj})


