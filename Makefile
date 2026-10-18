ROPS_HOME ?= /Users/mac/researchops

reproduce: run analyze claims lint preflight

run:
	rops-run grid .

analyze:
	@for f in $$(ls analysis/*.py 2>/dev/null | grep -v '/figures\.py$$' | sort); do \
		echo "== $$f"; PYTHONPATH=$(ROPS_HOME) python3 $$f || exit 1; \
	done

claims:
	rops-claims build .

lint:
	rops-lint paper/paper.md

preflight:
	rops-preflight .

guard:
	rops-guard check .

# ---- Study 2 (confirmatory; runs during the sprint) -------------------------------------
KAGGLE_USER ?= ayodejiadesegun

study2-pack:
	rops-kaggle pack study2 --user $(KAGGLE_USER)

study2-sim:
	PYTHONPATH=$(ROPS_HOME) python3 -m rops.kaggle_sim study2 --conditions C8 C2 C3 --seeds 8 --rounds 2 \
		--python "uv run -q --with pydantic --with jinja2 --with numpy --with tqdm python"

study2-push:
	kaggle kernels push -p study2/kaggle --accelerator NvidiaTeslaT4

study2-push-alt:
	kaggle kernels push -p study2/kaggle-alt --accelerator NvidiaTeslaT4

study2-status:
	-kaggle kernels status $(KAGGLE_USER)/study2-rops
	-kaggle kernels status $(KAGGLE_USER)/study2-rops-alt

study2-pull:
	rops-kaggle pull study2

study2-analyze: analyze
	python3 analysis/figures.py
	rops-claims build .
