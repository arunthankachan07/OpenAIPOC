from django.shortcuts import render
import openai

# Create your views here.
def index(request):
    return render(request,"paraphrase/index.html")


def paraphraseText(request):
    if request.method=='POST':
        text=request.POST.get('textbox')
        # Use your OpenAI API key
        openai.api_key = "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"
        # Use the OpenAI API to generate a paraphrase
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Paraphrase the sentence: {text}",
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
        )
        # Extract the paraphrased text from the API response
        paraphrased_text = response["choices"][0]["text"]
        return render(request,'paraphrase/paraphrase.html', {"text": paraphrased_text,"prompttext":text})
    return render(request,"paraphrase/paraphrase.html")


def summarizeText(request):
    if request.method=='POST':
        text=request.POST.get('textbox')
        # Use your OpenAI API key
        openai.api_key = "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"
        # Use the OpenAI API to generate a paraphrase
        response = openai.Completion.create(
        model="text-davinci-002",
        # prompt=f"{text}+\n\nTl;dr",
        prompt=(f"summarize: {text}"),
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
        )
        # Extract the paraphrased text from the API response
        summarized_text = response["choices"][0]["text"]
        return render(request,'paraphrase/paraphrase.html', {"text": summarized_text,"prompttext":text})
    return render(request,"paraphrase/summarize.html")
   