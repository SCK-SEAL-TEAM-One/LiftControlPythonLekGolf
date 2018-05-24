import unittest
import Lift as lift
class TeseCase(unittest.TestCase):

    #=============Testcase isOverWeight===============
    def test_over_weight_lower(self):
        result = lift.isWeightOver(999,1000)
        self.assertFalse(result, False)

    def test_over_weight_equal(self):
        result = lift.isWeightOver(1000,1000)
        self.assertFalse(result, False)

    def test_over_weight_over(self):
        result = lift.isWeightOver(1001,1000)
        self.assertTrue(result, True)

    #=============Testcase controlLift===============
    def test_control_lift_same_floor(self):
        lift.current_floor = 1
        result = lift.controlLift(1)
        self.assertEqual(result, 1)

    def test_control_lift_up_floor(self):
        lift.current_floor = 1
        result = lift.controlLift(5)
        self.assertEqual(result, 5)

    def test_control_lift_down_floor(self):
        lift.current_floor = 5
        result = lift.controlLift(2)
        self.assertEqual(result, 2)

    def test_control_lift_Over_Top_floor(self):
        lift.current_floor = 2
        result = lift.controlLift(11)
        self.assertEqual(result, 2)

    def test_control_lift_Lower_Lowest_floor(self):
        lift.current_floor = 2
        result = lift.controlLift(0)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
