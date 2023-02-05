from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'finder/home.html')

def pred(request):
    return render(request, 'finder/pred.html')

def finder(request):

    import pickle as p

    f = open("finder/trained_bert.dat", 'rb+')
    model = p.load(f)
    if request.method == 'POST':

        context = request.POST["context"]
        question = request.POST["question"]
        answer = model(context=context, question=question)


    return render(request, 'finder/finder.html', {'ans':answer['answer'], "ques":question})