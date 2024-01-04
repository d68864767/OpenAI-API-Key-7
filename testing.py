```python
# Importing necessary libraries
from tensorflow_data_validation.utils import slicing_util
from tensorflow_data_validation import StatsOptions
from tensorflow_data_validation import validate_statistics
from great_expectations import DataContext
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

def run():
    # TensorFlow Data Validation (TFDV)
    tfdv_options = StatsOptions(slicing_functions=[slicing_util.get_feature_value_slicer(features={'feature_name': None})])
    tfdv_stats = tfdv.generate_statistics_from_csv(data_location='path_to_your_data.csv', stats_options=tfdv_options)
    anomalies = tfdv.validate_statistics(statistics=tfdv_stats, schema=schema)
    tfdv.display_anomalies(anomalies)

    # Great Expectations
    context = DataContext('great_expectations.yml')
    batch = context.get_batch('my_datasource', 'my_generator', 'my_asset')
    expectation_suite = context.get_expectation_suite('my_expectation_suite')
    validation_result = context.run_validation_operator('action_list_operator', assets_to_validate=[batch], expectation_suite_name='my_expectation_suite')

    # TFX (TensorFlow Extended)
    context = InteractiveContext()
    example_gen = CsvExampleGen(input_base='path_to_your_data')
    context.run(example_gen)

if __name__ == "__main__":
    run()
```
