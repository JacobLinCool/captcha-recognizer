import os

raw_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))

if not os.path.exists(raw_dir):
    os.makedirs(raw_dir)

preprocess_dir = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "data", "preprocessed")
)

if not os.path.exists(preprocess_dir):
    os.makedirs(preprocess_dir)

genereated_dir = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "data", "generated")
)

if not os.path.exists(genereated_dir):
    os.makedirs(genereated_dir)
