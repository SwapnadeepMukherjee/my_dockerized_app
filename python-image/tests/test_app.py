import os
import subprocess
import sys


def test_app_prints_expected_message_and_directory():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(test_dir, ".."))
    result = subprocess.run(
        [sys.executable, os.path.join(project_dir, "app.py")],
        cwd=project_dir,
        capture_output=True,
        text=True,
        check=True,
    )

    print(f"--- DEBUG STDOUT ---\n{result.stdout}\n-------------------")
    assert "This is my second personal Dockerized Python App " in result.stdout
    assert "Current working directory:" in result.stdout
    assert "app.py" in result.stdout
    assert "Files in current directory:" in result.stdout