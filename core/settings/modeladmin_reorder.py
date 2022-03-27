ADMIN_REORDER = [
    { 'app': 'library', 'models': [ 'categories.Category', 'library.Author', 'library.Book', 'library.Borrow' ]},
    { 'app': 'quiz', 'models': [ 'quiz.QuizResult' ]},
    { 'app': 'management', 'models': [ 'management.Student', 'management.Course', 'management.Subject' ]},
    {'app': 'auth', 'label': 'Authentication and Authorization', 'models': ['accounts.User', 'auth.Group'] },
    { 'app': 'constance', 'label': 'App Setting', 'models': [ 'constance.Config' ] }
]
