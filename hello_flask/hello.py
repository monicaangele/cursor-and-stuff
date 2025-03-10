from flask import Flask, render_template, request
import random
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')

@app.route('/hello')
def hello():
   page = """
      <h1>Here's a random number: {0}</h1>
      <form>
         <button>New Number</button>
      </form>
   """
   num = random.randint(1, 25)
   return page.format(num)

@app.route('/goodbye')
def goodbye():
   message = "<h2>This is the second page!</h2>"
   return message 

@app.route('/results', methods=["POST"])
def results():
   color_choice = request.form['color']
   fav_num = request.form['lucky_number']
   fav_class = request.form['fav_class']
   fav_pix = request.form['best_pix'].lower().strip()
   films = ["toy story","a bug's life","toy story 2","monsters, inc.",
      "finding nemo", "the incredibles","cars","ratatouille","wall-e","up",
      "toy story 3","cars 2", "brave","monsters university","inside out",
      "the good dinosaur","finding dory", "cars 3","coco","incredibles 2",
      "toy story 4","onward","soul"]
   if fav_pix not in films:
      fav_pix = "Sorry, '{0}' isn't a Pixar film.".format(fav_pix.title())
   else:
      fav_pix = fav_pix.title()

   return render_template('form_results.html', color = color_choice, lucky_number = fav_num, fav_class = fav_class, best_pix = fav_pix)

@app.route('/third_page')
def third_page():
   message = "<h2>This is the third page!</h2>"
   return message

@app.route('/form')
def form():
   return render_template("favorite_form.html")

@app.route('/thanks')
def thanks():
   person = "Bob"
   gift = "wand"
   verb = "playing"
   noun = "ninja"
   closing_word = "Sincerely"
   author = "Bob"
   return render_template("tynote.html", name = person, gift = gift, verb = verb, noun = noun, closing_word = closing_word, author = author)

if __name__ == '__main__':
   app.run()