# Ubiquitous Octo Invention

Given a photo, return relevant documents.

Requirements:
pdf2image
Tesseract


I began with the objective of building a Doc2Vec model of the JFK Assassination archive to see if I could, from a photo of a convertible on a hill and Azure's computer vision service, return some vaguely relevant records. It turned out the image quality of most of the JFK records–1970s era photocopies–was so bad that even I had a hard time reading some of them myself. But I pressed on nevertheless. Of course the rest of the pipeline's performance ended up falling short of what I'd hoped for. But I'm reasonably certain that was a garbage in, garbage out problem. Given my previous experience with Gensim's Doc2Vec implementation I'm quite hopeful that a more intelliglbe corpus would yield a much more interesting search engine.