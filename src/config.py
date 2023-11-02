# I. Set the environment to "dev" or "prod"
ENV = "prod"

DATA_DIR = "data"
MODELS_DIR = "models"
RESULTS_DIR = "results"
LOGS_DIR = "logs"

# II. The following are used for training
SAMPLE_SIZE = None
REUSE_PREPROCESSED_DATA = True
REUSE_PREGENERATED_EMBEDDINGS = True

CONNECTION_STRING = "enter-your-connection-string"

# Choose to section text by sentences or paragraphs
# It can take values from ["sentence", "paragraph", None]
TEXT_SECTION_TYPE = None
assert TEXT_SECTION_TYPE in ["sentence", "paragraph", None], "TEXT_SECTION_TYPE can only take values from ['sentence', 'paragraph', None]"

# Define the input types for the training data.
# It can be either ["title"] or ["text"] or both ["title", "text"]
TRAIN_DATA_INPUT_TYPES = ["title"]
TRAIN_DATA_INPUT_TYPES.sort(reverse=True)
SEARCH_INDEX_TYPE = "annoy"
assert SEARCH_INDEX_TYPE in ["annoy"], "SEARCH_INDEX_TYPE can only take values from ['annoy', 'faiss']"
ANNOY_N_TREES = 50
ANNOY_METRIC = "euclidean"  # "manhattan", "angular"
SEARCH_INDEX = f"{TEXT_SECTION_TYPE}_" + "_".join(TRAIN_DATA_INPUT_TYPES) + f".{SEARCH_INDEX_TYPE}"
if TEXT_SECTION_TYPE == "sentence":
    assert "title" not in TRAIN_DATA_INPUT_TYPES, "title is not supported for sentence section type"

# Define model type for SentenceTransformer
# It can take values from https://www.sbert.net/docs/pretrained_models.html
SENTENCE_TRANSFORMER_MODEL_TYPE = "all-MiniLM-L6-v2"
if SENTENCE_TRANSFORMER_MODEL_TYPE == "all-MiniLM-L6-v2":
    ANNOY_SIZE = 384
elif SENTENCE_TRANSFORMER_MODEL_TYPE == "distilbert-base-nli-stsb-mean-tokens":
    ANNOY_SIZE = 768
elif SENTENCE_TRANSFORMER_MODEL_TYPE == "bert-base-nli-mean-tokens":
    ANNOY_SIZE = 768
else:
    raise Exception("Invalid SENTENCE_TRANSFORMER_MODEL_TYPE")

# III. The following are used for inference
RELEVANCE_SCORE_ROUNDING = 2
RELEVANCE_SCORE_THRESHOLD = 0.4
