from pathlib import Path

from lenslog import definition as d

ROOT = Path(__file__).resolve().parents[3]


def test_surveyor_definition():
    defn = d.load(ROOT)
    assert defn.module == "surveyor"
    m = lambda p, k="write": d.match_path(defn, p, k)  # noqa: E731
    assert m("C:/Users/Liz/PROVES_LIBRARY/canon/ONTOLOGY.md", "read") == {"source"}
    assert m("C:/Users/Liz/proves-curation-dashboard/src/hooks/useLibrary.ts", "read") == {"source"}
    assert m(str(ROOT / "CHARTER.md")) == {"identity"}
    assert m(str(ROOT / "docs" / "BUILD.md")) == {"identity"}
    assert m(str(ROOT / "decomposition.json")) == {"definition"}
    assert m(str(ROOT / "skills" / "decomposition" / "SKILL.md")) == {"method"}
    assert m(str(ROOT / "docs" / "decomposition" / "evaluations" / "x.md")) == {"evaluations"}
    assert m(str(ROOT / "docs" / "decomposition" / "proves" / "module-map.md")) == {"cases"}
    assert m(str(ROOT / "plugins" / "lens-log" / "scripts" / "stop_check.py")) == {"tooling"}
    assert m(str(ROOT / "README.md")) == set()
    assert m(str(ROOT / "docs" / "log" / "entries" / "x.md")) == set()
