all: index.json
	
index.json: assets
	python index.py $< | tee $@

.PHONY: index.json

clean:
	rm -f index.json

update:
	bundle update

serve: update index.json
	bundle exec jekyll serve
