from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # List any dependencies here
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',  # Ensure that `math_quiz.py` contains a `main()` function
        ],
    },
)
