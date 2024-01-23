from django.shortcuts import render
from .forms import fourLetterWordForm
import json
from wonderwords import RandomWord


# Create your views here.
def letter_in_word(guess_word, answer_word):
    matched_indices = set()
    match_status = []

    for index in range(len(answer_word)):
        if guess_word[index] == answer_word[index]:
            matched_indices.add(index)
            match_status.append("Match")
        elif guess_word[index] in answer_word and index not in matched_indices:
            match_status.append("Exists")
        else:
            match_status.append("NoMatch")

    return match_status


answer_word = RandomWord()
new_answer_word = answer_word.word(word_min_length=4, word_max_length=4)


correctly_guessed_letters = set()


def index_view(request):
    answer = new_answer_word.upper().strip()
    print(answer)

    match_status = []
    match_status_with_css = []
    match_status_with_csss = []

    current_guess = 1

    if request.method == "POST":
        input_form = fourLetterWordForm(request.POST)
        if input_form.is_valid():
            letter_one = input_form.cleaned_data.get("letterOne")
            letter_two = input_form.cleaned_data.get("letterTwo")
            letter_three = input_form.cleaned_data.get("letterThree")
            letter_four = input_form.cleaned_data.get("letterFour")

            guess_list = [letter_one, letter_two, letter_three, letter_four]

            guess_trials = len(guess_list)

            guess_word = "".join(guess_list).lower().strip()

            print(f"Guess word: {guess_word}")
            print(f"Answer word: {new_answer_word}")

            match_status = letter_in_word(guess_word, new_answer_word)
            css_classes = {
                "Match": "border-green-500 text-green-500",
                "Exists": "border-yellow-400 text-yellow-400",
                "NoMatch": "border-red-600 text-red-600",
            }

            csss_classes = {
                "Match": "green",
                "Exists": "yellow",
                "NoMatch": "red",
            }

            correctly_guessed_letters.update(
                index for index, status in enumerate(match_status) if status == "Match"
            )

            match_status_with_css = [
                css_classes.get(status, "bg-transparent") for status in match_status
            ]
            match_status_with_csss = [
                csss_classes.get(status, "transparent") for status in match_status
            ]

            show_new_row = False
            hide_new_row = False
            print(match_status_with_css)
            # print(input_form.visible_fields())
            if any(
                status
                in (
                    "border-red-600 text-red-600",
                    "red",
                    "border-yellow-400 text-yellow-400",
                    "yellow",
                )
                for status in (match_status_with_css + match_status_with_csss)
            ):
                show_new_row = True
                # Keep the current form for the existing row
                current_form = input_form

            else:
                show_new_row = False
                hide_new_row = True
                current_form = input_form
            return render(
                request,
                "fourLetters/index.html",
                {
                    "form": current_form,
                    "match_status_with_css": match_status_with_css,
                    "match_status_with_csss": match_status_with_csss,
                    "show_new_row": show_new_row,
                    "hide_new_row": hide_new_row,
                    "correctly_guessed_letters": correctly_guessed_letters,
                },
            )

    else:
        input_form = fourLetterWordForm()

    return render(
        request,
        "fourLetters/index.html",
        {
            "form": input_form,
            "match_status_with_css": match_status_with_css,
            "match_status_with_csss": match_status_with_csss,
            "show_new_row": False,
            "hide_new_row": False,
            "correctly_guessed_letters": correctly_guessed_letters,
        },
    )
