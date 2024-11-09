from flask import render_template, jsonify, request, flash
from app.main import bp
from datetime import datetime

# Agregar contexto global para todas las templates
@bp.context_processor
def utility_processor():
    return {
        'current_year': datetime.utcnow().year
    }

@bp.route('/')
def index():
    user = {'username': 'Usuario'}
    posts = [
        {'author': 'Juan', 'body': 'Hermoso día en Barcelona!'},
        {'author': 'María', 'body': 'Me encanta Python!'}
    ]
    return render_template('index.html', title='Inicio', user=user, posts=posts)

@bp.route('/about')
def about():
    return render_template('about.html', title='Sobre Nosotros')

@bp.route('/load-more-posts')
def load_more_posts():
    # Simular carga de más posts
    new_posts = [
        {'author': 'Carlos', 'body': '¡HTMX es increíble!'},
        {'author': 'Ana', 'body': 'Aprendiendo Tailwind CSS'}
    ]
    return render_template('_posts.html', posts=new_posts)

@bp.route('/like-post/<int:post_id>', methods=['POST'])
def like_post(post_id):
    # Simular like de un post
    return """
        <button class="mt-4 inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-full shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
            ¡Me gusta!
        </button>
    """

@bp.route('/contact', methods=['POST'])
def contact():
    email = request.form.get('email')
    message = request.form.get('message')
    # Aquí procesarías el formulario de contacto
    flash('Mensaje enviado correctamente', 'success')
    return render_template('about.html', title='Sobre Nosotros')