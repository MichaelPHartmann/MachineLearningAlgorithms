from math import log

class attributeSelectionMeasures():

    def init(self):
        pass

    def single_attribute_entropy(self, frequencies):
        # Takes a list of frequencies
        freq_sum = sum(frequencies)
        running_entropy = 0
        for f in frequencies:
            if f != 0:
                p = f / freq_sum
                entropy_calc = -(p * log(p, 2))
                running_entropy += entropy_calc
            else:
                pass
        return running_entropy

    def double_attribute_entropy(self, frequencies_ab):
        # FORMAT VERY IMPORTANT
        # List of lists creating an array
        # Each list is the frequency of the x attribute for the y attributes
        # [
        # [2,8,4,9],
        # [6,3,7,1],
        # [9,4,6,2]
        # ]
        table_sum = 0
        table_entropy = 0
        for l in frequencies_ab:
            table_sum += sum(l)
        for x_attr in frequencies_ab:
            row_sum = sum(x_attr)
            row_entropy = self.single_attribute_entropy(x_attr)
            table_entropy += (row_sum / table_sum) * row_entropy
        return table_entropy

    def sample_variance(self, nums):
        mean = sum(nums) / len(nums)
        n = len(nums)
        sum_squared_differences = 0
        for num in nums:
            sum_squared_differences += (num - mean)**2
        variance_result = sum_squared_differences / (n - 1)
        return variance_result

    def gini_index(self, nums):
        # This works best on labels of data. The data can be numbers or strings.
        running_total = 0
        n = len(nums)
        classes = {}
        for num in nums:
            if num in classes.keys():
                classes[num] += 1
            else:
                classes[num] = 1
        for c, freq in classes.items():
            probability = freq / n
            running_total += probability**2
        return 1 - running_total

    def chi_square(self, category_dict):
        # Takes a dictionary that uses the category as the key, and frequency as the value.
        observation_frequencies = category_dict.values()
        number_observations = sum(observation_frequencies)
        expected = number_observations / len(category_dict.keys())
        running_total = 0
        for observed in observation_frequencies:
            equation = ((observed - expected)**2) / expected
            running_total += equation
        return running_total
