shell: 
	gitbook build
	gh-pages -d _book
clean:
	rm -rf _book