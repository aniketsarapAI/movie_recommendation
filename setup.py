REPO_NAME = "Personalized-Movie-Recommendation-System"
AUTHOR_USER_NAME = "aniketsarap"
SRC_REPO = "movie_recommender"
LIST_OF_REQUIREMENTS = ['streamlit', 'scikit-learn', 'numpy', 'pandas']

setup(
    name=SRC_REPO,
    version="0.0.2",
    author=AUTHOR_USER_NAME,
    description="A personalized package for a Movie Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="aniketsarap27@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)
