from transformers import pipeline
import time
from forms import Search
from flask import render_template, request, flash
from config import content


@content.route('/', methods=['GET', 'POST'])
def index():
    form = Search()
    if request.method == "POST":
        try:
            text = request.form.get("search")
            maximum = int(request.form.get("max"))
            minimum = int(request.form.get("min"))
            start = time.perf_counter()
            generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
            result = generator(text, max_length=maximum, min_length=minimum, do_sample=True, temperature=0.9)
            result = result[0]["generated_text"]
            end = time.perf_counter()
            print(result)
            print((end - start))
            return render_template('index.html', form=form, result=result)

        except:
            msg = "Pls try again"
            return render_template('index.html', form=form, msg=msg)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    content.run(debug=True)
