import os
import subprocess
import sys


def test_app_prints_expected_message_and_directory():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    result = subprocess.run(
        [sys.executable, os.path.join(project_dir, "app.py")],
        cwd=project_dir,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "This is my second personal Dockerized Python App " in result.stdout
    assert "Current working directory:" in result.stdout
    # assert "app.py" in result.stdout
    assert "Files in current directory:" in result.stdout