"""M1, M3, M4, M5 from the deferred-defects list (roadmap item lens-log-remaining-defects)."""
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import record_touch  # noqa: E402
import stop_check  # noqa: E402
from conftest import SAMPLE  # noqa: E402
from lenslog import entries  # noqa: E402

NOW = datetime(2026, 10, 22, 8, 0, 0)


def write(repo, path, cwd=None, tool="Write"):
    record_touch.handle({"session_id": "s1", "cwd": str(cwd or repo), "tool_name": tool,
                         "tool_input": {"file_path": path}})


def stop(cwd):
    return {"session_id": "s1", "cwd": str(cwd), "hook_event_name": "Stop",
            "stop_hook_active": False, "last_assistant_message": "done"}


def test_m1_block_message_names_the_running_interpreter(repo):
    write(repo, str(repo / "CHARTER.md"))
    out = stop_check.decide(stop(repo), NOW)
    assert f'"{sys.executable}"' in out["reason"]
    assert ' python "' not in out["reason"]


def test_m3_touches_in_one_repo_do_not_count_in_another(repo, tmp_path):
    other = tmp_path / "lens-other"
    other.mkdir()
    (other / "decomposition.json").write_text(json.dumps(dict(SAMPLE, module="lens-other")),
                                              encoding="utf-8")
    write(repo, str(repo / "CHARTER.md"))
    assert stop_check.decide(stop(other), NOW) is None
    assert stop_check.decide(stop(repo), NOW)["decision"] == "block"


def test_m4_relative_paths_resolve_from_the_working_directory(repo):
    (repo / "docs").mkdir()
    write(repo, "schema/spine.sql", cwd=repo / "docs")
    out = stop_check.decide(stop(repo / "docs"), NOW)
    assert out and "bus" in out["reason"]


def test_m5_misses_in_the_same_second_do_not_overwrite(repo):
    first = entries.write_missed(repo, {"identity": ["a"]}, "s1", NOW)
    second = entries.write_missed(repo, {"bus": ["b"]}, "s1", NOW)
    assert first != second and first.exists() and second.exists()
    assert json.loads(first.read_text(encoding="utf-8"))["surfaces"] == {"identity": ["a"]}
