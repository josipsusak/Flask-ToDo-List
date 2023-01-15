from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from datetime import date
from forms import EntryForm, TodoForm
from models import db, Entry
import os

app = Flask(__name__)
Bootstrap(app)

# Configure database
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", 'sqlite:///todo_list.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app=app)
app.app_context().push()
db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    entry_form = EntryForm()
    if request.method == "POST":
        str_date = "-".join(request.form.get("due_date").split("-")[::-1])
        new_entry = Entry(
            todo_text=entry_form.todo_text.data,
            added_date=date.today().strftime("%d-%m-%Y"),
            due_date=str_date,
            finished=request.form.get("finished")
        )
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for("home"))
    todo_posts = Entry.query.all()
    post_form = TodoForm()
    return render_template("index.html", form=entry_form, post_form=post_form, posts=todo_posts)


@app.route("/delete/int:<post_id>")
def delete(post_id):
    delete_post = Entry.query.get(post_id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/toggle_checkbox/int:<post_id>")
def toggle(post_id):
    post_status = Entry.query.get(post_id)
    post_status.finished = True
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
