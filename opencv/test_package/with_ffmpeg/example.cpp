#include <iostream>
#include <vector>
#include "opencv2/aruco/charuco.hpp"
#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/videoio.hpp"

using namespace cv;

int main() {
  std::cout << " ########################## RUNNING WITH_FFMPEG TEST ##########################"
            << std::endl;

  cv::Mat m = cv::Mat::ones(2, 2, CV_8UC3);
  cv::VideoCapture video("../../../big_buck_bunny_720p_1mb.mp4");
  if (!video.isOpened()) {
    std::cout << "failed to open video" << std::endl;
    return -1;
  }

  cv::Mat frame;
  video >> frame;

  std::vector<unsigned char> buffer;
  if (frame.empty()) {
    std::cout << "empty frame" << std::endl;
    return -1;
  }

  cv::imencode(".jpeg", frame, buffer);

  int squaresX = 5;
  int squaresY = 7;
  int squareLength = 200;
  int markerLength = 150;
  int dictionaryId = 0;
  int margins = squareLength - markerLength;
  int borderBits = 1;

  Ptr<aruco::Dictionary> dictionary =
      aruco::getPredefinedDictionary(aruco::PREDEFINED_DICTIONARY_NAME(dictionaryId));

  Size imageSize;
  imageSize.width = squaresX * squareLength + 2 * margins;
  imageSize.height = squaresY * squareLength + 2 * margins;

  Ptr<aruco::CharucoBoard> board = aruco::CharucoBoard::create(
      squaresX, squaresY, (float)squareLength, (float)markerLength, dictionary);

  // show created board
  Mat boardImage;
  board->draw(imageSize, boardImage, margins, borderBits);

  imwrite("charuco.png", boardImage);
}
