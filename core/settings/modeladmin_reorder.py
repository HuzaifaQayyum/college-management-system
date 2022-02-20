ADMIN_REORDER = [
    { 'app': 'library', 'models': [ 'library.Author', 'library.Book', 'library.Borrow' ]},
    { 'app': 'quiz', 'models': [ 'quiz.QuizResult' ]},
    { 'app': 'categories', 'models': [ 'categories.Category' ]},
    { 'app': 'core', 'models': [ 'core.Student', 'core.Course', 'core.Subject' ]},
    {'app': 'auth', 'label': 'Authentication and Authorization', 'models': ['accounts.User', 'auth.Group'] },
    { 'app': 'constance', 'label': 'App Setting', 'models': [ 'constance.Config' ] }
]
