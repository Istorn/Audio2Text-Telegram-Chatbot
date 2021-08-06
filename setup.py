from setuptools import setup, find_packages

setup(
    name='audio2texttelegram',
    version='1.0.0',
    package_dir={'': 'src'},
    packages=find_packages(where="src"),
    
    
    license='CC BY-NC 4.0',
    description='Telegram chatbot able to convert audio messages into texts through Google Cloud Speech APIs.',
    long_description=open('README_IT.md').read(),
    install_requires=[],
    url='https://github.com/Istorn/Audio2Text-Telegram-Chatbot',
    author='Lorenzo Neri',
    author_email='hello@lorenzoneri.com'
)