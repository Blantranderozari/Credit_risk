"""Transform module
"""

import tensorflow as tf
import tensorflow_transform as tft

CATEGORICAL_FEATURES = {
    "person_home_ownership": 4,
    "loan_intent": 6,
    "loan_grade": 7
}
NUMERICAL_FEATURES = [
    "person_age",
    "person_income",
    "person_emp_length",
    "loan_amnt",
    "loan_int_rate",
    "loan_status",
    "loan_percent_income",
    "cred_hist_length"
]
LABEL_KEY = "cb_person_default_on_file"

def transformed_name(key):
    """Renaming transformed features"""
    return key + '_xf'

def convert_num_to_one_hot(label_tensor, num_labels=2):
    """
    Convert  a label (0 or 1) into a one-hot vector
    Args:
        int: label_tensor (0 or 1)
    Returns:
        label tensor
    """
    one_hot_tensor = tf.one_hot(label_tensor, num_labels)
    return tf.reshape(one_hot_tensor, [-1, num_labels])


def preprocessing_fn(inputs):
    """
    Preprocess input features into transformed features

    Args:
        inputs: map from feature keys to raw features

    Return:
        outputs: map from feature keys to transformed feature
    """

    outputs = {}

    for key, dim in CATEGORICAL_FEATURES.items():
        int_value = tft.compute_and_apply_vocabulary(
            inputs[key], top_k=dim
        )
        outputs[transformed_name(key)] = convert_num_to_one_hot(
            int_value, num_labels=dim
        )

    for feature in NUMERICAL_FEATURES:
        outputs[transformed_name(feature)] = tft.scale_to_z_score(inputs[feature])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY],tf.int64)

    return outputs
