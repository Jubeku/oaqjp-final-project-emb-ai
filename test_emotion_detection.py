import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test case for joy
        response1 = emotion_detector('I am glad this happened')
        self.assertEqual(response1['dominant_emotion'], 'joy')

        # Test case for anger
        response2 = emotion_detector('I am really mad about this')
        self.assertEqual(response2['dominant_emotion'], 'anger')

        # Test case for disgust
        response3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(response3['dominant_emotion'], 'disgust')

        # Test case for sadness
        response4 = emotion_detector('I am so sad about this')
        self.assertEqual(response4['dominant_emotion'], 'sadness')

        # Test case for fear
        response5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(response5['dominant_emotion'], 'fear')


unittest.main()