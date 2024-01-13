from setuptools import find_packages, setup

setup(
    name="github_poster",
    author="yihong0618",
    author_email="zouzou0208@gmail.com",
    url="https://github.com/yihong0618/GitHubPoster",
    license="MIT",
    version="2.7.2",
    description="Make everything a GitHub svg poster and Skyline!",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "svgwrite",
        "pendulum==3.0.0",
        "colour",
    ],
    extras_require={
        "garmin": ["garminconnect"],
        "gpx": ["gpxpy"],
        "strava": ["stravalib"],
        "github": ["PyGithub"],
        "skyline": ["sdf_fork"],
        "todoist": ["pandas"],
        "all": [
            "twint_fork",
            "garminconnect",
            "gpxpy",
            "stravalib==1.5",
            "PyGithub",
            "sdf_fork",
            "pandas",
        ],
    },
    entry_points={
        "console_scripts": ["github_poster = github_poster.cli:main"],
    },
)
