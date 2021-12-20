class singleLinearRegression():

    def __init__(self, x, y):
        self.n = len(y)
        self.x = x
        self.x_sum = sum(x)
        self.x_square_sum = self.sum_of_squares(x)
        self.y = y
        self.y_sum = sum(y)
        self.y_square_sum = self.sum_of_squares(y)
        self.x_y_sum = self.sum_of_xy(x,y)
        self.calculate_slope()
        self.calculate_y_intercept()

    def sum_of_squares(self, nums):
        result = 0
        for n in nums:
            result += (n**2)
        return result

    def sum_of_xy(self, x, y,):
        result = 0
        for i in range(self.n):
            result += (x[i] * y[i])
        return result

    def calculate_slope(self): #b1
        numerator = (self.n * self.x_y_sum) - (self.x_sum * self.y_sum)
        denominator = ((self.n * self.x_square_sum) - (self.x_sum**2))
        self.sample_slope = numerator / denominator
        return self.sample_slope

    def calculate_y_intercept(self): # b0
        numerator = (self.y_sum * self.x_square_sum) - (self.x_sum * self.x_y_sum)
        denominator = ((self.n * self.x_square_sum) - (self.x_sum**2))
        self.y_intercept = numerator / denominator
        return self.y_intercept

    def estimate_point(self, x):
        y = (self.sample_slope * x) + self.y_intercept
        coordinate = (x, y)
        return coordinate


class multipleLinearRegression():

    def __init__(self, x_variables, y):
        self.x_variables_raw = x_variables
        self.y = y
        self.data_integrity_checks()
        self.n = len(y)
        self.num_x_vars = len(x_variables)
        self.y_mean = sum(y) / len(y)
        self.x_variable_objects = []
        self.create_x_variable_attributes()
        self.calculate_y_intercept()

    class x_variable():
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y
            self.mean = sum(x) / len(x)
            self.sample_variance(x)
            self.sample_covariance(x, y)
            self.beta_coefficient = self.covariance / self.variance

        def sample_variance(self, nums):
            mean = sum(nums) / len(nums)
            n = len(nums)
            sum_squared_differences = 0
            for num in nums:
                sum_squared_differences += (num - mean)**2
            variance_result = sum_squared_differences / (n - 1)
            self.variance = variance_result # Only line that is not generic
            return variance_result

        def sample_covariance(self, x, y):
            x_mean = sum(x) / len(x)
            y_mean = sum(y) / len(y)
            n = len(x)
            multiplied_differences = 0
            for i in range(n):
                x_diff = x[i] - x_mean
                y_diff = y[i] - y_mean
                multiplied_differences += (x_diff * y_diff)
            covariance_result = multiplied_differences / (n - 1)
            self.covariance = covariance_result # Only line that is not generic
            return covariance_result

    def data_integrity_checks(self):
        length_y = len(self.y)
        for x_var in self.x_variables_raw:
            if len(x_var) != length_y:
                raise Exception(F"Variable lists must be the same length as the y variable list!\nLength X: {len(x_var)}, Length Y: {length_y}")
            for v in x_var:
                if not type(v) is int:
                    if not type(v) is float:
                        raise TypeError("Variable data points must be integers or floats!")

    def create_x_variable_attributes(self):
        for i, x in enumerate(self.x_variables_raw):
            dummy = self.x_variable(i+1, x, self.y)
            self.x_variable_objects.append(dummy)

    def calculate_y_intercept(self):
        x_variable_calcs = self.y_mean
        for var in self.x_variable_objects:
            calc = var.beta_coefficient * var.mean
            x_variable_calcs -= calc
        self.y_intercept = x_variable_calcs
        return x_variable_calcs

    def estimate_point(self, x_values):
        running_calcs = self.y_intercept
        coordinates = {"Vertical Intercept":self.y_intercept}
        for i, value in enumerate(x_values):
            new_calc = self.x_variable_objects[i].beta_coefficient * value
            running_calcs += new_calc
            coordinates[F"X{i+1}"] = new_calc
        coordinates["Y"] = running_calcs
        return coordinates


if __name__ == "__main__":
    c = singleLinearRegression([34,42,98,78,61],[15,72,38,27,94])
    print(c.estimate_point(100))

    b = multipleLinearRegression([[1,2,3,4,5,6,7,8,9],[2,4,6,8,10,12,14,16,18]], [13,52,55,74,85,94,123,366,568])
    print(b.estimate_point([10,12]))
