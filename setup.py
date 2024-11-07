from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.0',
        'pandas==1.3.0',
        'pytest==6.2.4'
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Ensure the `math_quiz.py` file has a `math_quiz()` function
        ],
    },
)
