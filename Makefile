all: index.json
	
index.json: assets
	python index.py $< | tee $@

clean:
	rm -f index.json

update:
	bundle update

serve: update
	bundle exec jekyll serve
