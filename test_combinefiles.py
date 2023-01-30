import unittest
from combinefiles import *
from pandas.testing import assert_frame_equal

class TestCombineFiles(unittest.TestCase):
    def test_combine_accessories_clothing(self):
        #Check combined has same columns as original
        combined = combine_csv_files(['combinefiles.py', 'fixtures/accessories.csv', 'fixtures/clothing.csv'])
        #Load original dataframes
        clothing_df = pd.read_csv('fixtures/clothing.csv')
        accessories_df = pd.read_csv('fixtures/accessories.csv')
        #Drop rows from combined that don't match specific file, drop the file column
        combined_clothing = combined[combined['filename'] == 'clothing.csv'].drop('filename', axis=1)
        assert_frame_equal(clothing_df, combined_clothing)
        combined_accessories = combined[combined['filename'] == 'accessories.csv'].drop('filename', axis=1)
        assert_frame_equal(accessories_df, combined_accessories)
    def test_combine_accessories_household(self):
        combined = combine_csv_files(['combinefiles.py', 'fixtures/accessories.csv', 'fixtures/household_cleaners.csv'])
        household_df = pd.read_csv('fixtures/household_cleaners.csv')
        accessories_df = pd.read_csv('fixtures/accessories.csv')
        #Drop rows from combined that don't match specific file, drop the file column
        combined_household = combined[combined['filename'] == 'household_cleaners.csv'].drop('filename', axis=1)
        assert_frame_equal(household_df, combined_household)
        combined_accessories = combined[combined['filename'] == 'accessories.csv'].drop('filename', axis=1)
        assert_frame_equal(accessories_df, combined_accessories)
    def test_combine_clothing_household(self):
        combined = combine_csv_files(['combinefiles.py', 'fixtures/clothing.csv', 'fixtures/household_cleaners.csv'])
        household_df = pd.read_csv('fixtures/household_cleaners.csv')
        clothing_df = pd.read_csv('fixtures/clothing.csv')
        #Drop rows from combined that don't match specific file, drop the file column
        combined_household = combined[combined['filename'] == 'household_cleaners.csv'].drop('filename', axis=1)
        assert_frame_equal(household_df, combined_household)
        combined_clothing = combined[combined['filename'] == 'clothing.csv'].drop('filename', axis=1)
        assert_frame_equal(clothing_df, combined_clothing)
    def test_combine_all_fixtures(self):
        #Check combined has same columns as original
        combined = combine_csv_files(['combinefiles.py', 'fixtures/accessories.csv', 'fixtures/clothing.csv', 'fixtures/household_cleaners.csv'])
        #Load original dataframes
        clothing_df = pd.read_csv('fixtures/clothing.csv')
        accessories_df = pd.read_csv('fixtures/accessories.csv')
        household_cleaners_df = pd.read_csv('fixtures/household_cleaners.csv')
        #Drop rows from combined that don't match specific file, drop the file column
        combined_clothing = combined[combined['filename'] == 'clothing.csv'].drop('filename', axis=1)
        assert_frame_equal(clothing_df, combined_clothing)
        combined_accessories = combined[combined['filename'] == 'accessories.csv'].drop('filename', axis=1)
        assert_frame_equal(accessories_df, combined_accessories)
        combined_household = combined[combined['filename'] == 'household_cleaners.csv'].drop('filename', axis=1)
        assert_frame_equal(household_cleaners_df, combined_household)