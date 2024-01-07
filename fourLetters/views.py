from django.shortcuts import render
from .forms import fourLetterWordForm
import json


# Create your views here.
def letter_in_word(guess_word, answer_word):
    matched_indices = set()
    match_status = []

    for index in range(len(answer_word)):
        if guess_word[index] == answer_word[index]:
            matched_indices.add(index)
            match_status.append('Match')
        elif guess_word[index] in answer_word and index not in matched_indices:
            match_status.append('Exists')
        else:
            match_status.append('NoMatch')

    return match_status

def index_view(request):
    answer_word = "Trip"
    answer = answer_word.upper()

    match_status = []
    match_status_with_css = []
    match_status_with_csss = []
    show_new_row = False

    if request.method == "POST":
        input_form = fourLetterWordForm(request.POST)
        if input_form.is_valid():
            letter_one = input_form.cleaned_data.get("letterOne")
            letter_two = input_form.cleaned_data.get("letterTwo")
            letter_three = input_form.cleaned_data.get("letterThree")
            letter_four = input_form.cleaned_data.get("letterFour")

            guess_list = [letter_one, letter_two, letter_three, letter_four]
            guess_word = "".join(guess_list)

            match_status = letter_in_word(guess_word, answer)
            css_classes = {
                'Match': 'bg-green-300',
                'Exists': 'bg-yellow-300',
                'NoMatch': 'bg-red-300',
            }
            
            csss_classes = {
                'Match': 'green',
                'Exists': 'yellow',
                'NoMatch': 'red',
            }

            match_status_with_css = [css_classes.get(status, 'bg-transparent') for status in match_status]
            match_status_with_csss = [csss_classes.get(status, 'transparent') for status in match_status]
            print(match_status_with_css)
            # print(input_form.visible_fields())
            if 'bg-red-300' or 'red' or 'bg-yellow-300' or 'yellow' in (match_status_with_css or match_status_with_csss):
                show_new_row = True
                # Keep the current form for the existing row
                current_form = input_form
                # Create a new form for a new row
                new_form = fourLetterWordForm()
                return render(request, "fourLetters/index.html", {"form": current_form, "match_status_with_css": match_status_with_css, "match_status_with_csss": match_status_with_csss, "show_new_row": show_new_row})

    else:
        input_form = fourLetterWordForm()

    return render(request, "fourLetters/index.html", {"form": input_form, "match_status_with_css": match_status_with_css, "match_status_with_csss": match_status_with_csss, "show_new_row": show_new_row})