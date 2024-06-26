try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="quepy",
    version="0.4.1",
    description="A framework to convert natural language to database queries.",
    long_description=open('README.rst').read(),
    author="Rafael Carrascosa, Gonzalo Garcia Berrotaran",
    author_email="rafacarrascosa@gmail.com",
    url="https://github.com/machinalis/quepy",
    keywords=["regular expressions", "regexp", "re", "NLP",
              "natural language processing",
              "natural language interface to database", "sparql", "database",
              "interface", "quepy"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        ],
    packages=["quepy"],
    # moved requires for "refo" to ffbo.nlp_component to allow this package to
    # install with pip
    install_requires=["nltk", "SPARQLWrapper", "docopt", "spacy>=3.2.6,<4"],
    scripts=["scripts/quepy"]
)
