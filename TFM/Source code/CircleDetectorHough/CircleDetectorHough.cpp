#include "CircleDetectorHough.h"


//#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))


/****************************************************************************
                          PUBLIC METHODS
****************************************************************************/


/****************************************************************************
**
**
**
** Detects circles in the specified QImage
**
****************************************************************************/
Mat CircleDetectorHough::detect(string source, int min_r, int max_r)
{
  Mat src = imread(source);
  Mat binary = edges(src);
  Mat detection;
  //QImage detection = source.convertToFormat(QImage::Format_RGB888);
  
  /* build a vector to hold images in Hough-space for radius 1..max_r, where
  max_r is specified or the maximum radius of a circle in this image */
/*  if(min_r == 0)
  {
    min_r = 5;
  }
  
  if(max_r == 0)
  {
    max_r = MIN(source.width(), source.height()) / 2;
  }
  
  QVector<Image> houghs(max_r - min_r);
  
  for(unsigned int i = min_r; i < max_r; i++)
  {
*/    /* instantiate Hough-space for circles of radius i */
/*    Image &hough = houghs[i - min_r];
    hough.resize(binary.width());
    for(unsigned int x = 0; x < hough.size(); x++)
    {
      hough[x].resize(binary.height());
      for(unsigned int y = 0; y < hough[x].size(); y++)
      {
        hough[x][y] = 0;
      }
    }
*/    
    /* find all the edges */
/*    for(unsigned int x = 0; x < binary.width(); x++)
    {
      for(unsigned int y = 0; y < binary.height(); y++)
      {
*/        /* edge! */
/*        if(binary.pixelIndex(x, y) == 1)
        {
          accum_circle(hough, QPoint(x, y), i);
        }
      }
    }
 */   
    /* loop through all the Hough-space images, searching for bright spots, which
    indicate the center of a circle, then draw circles in image-space */
/*    unsigned int threshold = 4.9 * i;
    for(unsigned int x = 0; x < hough.size(); x++)
    {
      for(unsigned int y = 0; y < hough[x].size(); y++)
      {
        if(hough[x][y] > threshold)
        {
          draw_circle(detection, QPoint(x, y), i, Qt::yellow);
        }
      }
    }
  }
*/    
  return detection;
}


/****************************************************************************
               _           __                  __  __           __
     ___  ____(_)  _____ _/ /____   __ _  ___ / /_/ /  ___  ___/ /__
    / _ \/ __/ / |/ / _ `/ __/ -_) /  ' \/ -_) __/ _ \/ _ \/ _  (_-<
   / .__/_/ /_/|___/\_,_/\__/\__/ /_/_/_/\__/\__/_//_/\___/\_,_/___/
  /_/

****************************************************************************/


/****************************************************************************
**
** Author: Marc Bowes
**
** Accumulates a circle on the specified image at the specified position with
** the specified radius, using the midpoint circle drawing algorithm
**
** Adapted from: http://en.wikipedia.org/wiki/Midpoint_circle_algorithm
**
****************************************************************************/
/*void HoughCircleDetector::accum_circle(Image &image, const QPoint &position, unsigned int radius)
{
  int f = 1 - radius;
  int ddF_x = 1;
  int ddF_y = -2 * radius;
  int x = 0;
  int y = radius;
  
  accum_pixel(image, QPoint(position.x(), position.y() + radius));
  accum_pixel(image, QPoint(position.x(), position.y() - radius));
  accum_pixel(image, QPoint(position.x() + radius, position.y()));
  accum_pixel(image, QPoint(position.x() - radius, position.y()));
  
  while(x < y)
  {
    if(f >= 0)
    {
      y--;
      ddF_y += 2;
      f += ddF_y;
    }
    
    x++;
    ddF_x += 2;
    f += ddF_x;
    
    accum_pixel(image, QPoint(position.x() + x, position.y() + y));
    accum_pixel(image, QPoint(position.x() - x, position.y() + y));
    accum_pixel(image, QPoint(position.x() + x, position.y() - y));
    accum_pixel(image, QPoint(position.x() - x, position.y() - y));
    accum_pixel(image, QPoint(position.x() + y, position.y() + x));
    accum_pixel(image, QPoint(position.x() - y, position.y() + x));
    accum_pixel(image, QPoint(position.x() + y, position.y() - x));
    accum_pixel(image, QPoint(position.x() - y, position.y() - x));
  }
}
*/

/****************************************************************************
**
** Author: Marc Bowes
**
** Accumulates at the specified position
**
****************************************************************************/
/*void HoughCircleDetector::accum_pixel(Image &image, const QPoint &position)
{
*/  /* bounds checking */
/*  if(position.x() < 0 || position.x() >= image.size() ||
     position.y() < 0 || position.y() >= image[position.x()].size())
  {
    return;
  }
  
  image[position.x()][position.y()]++;
}
*/
/****************************************************************************
**
** Author: Marc Bowes
**
** Draws a circle on the specified image at the specified position with
** the specified radius, using the midpoint circle drawing algorithm
**
** Adapted from: http://en.wikipedia.org/wiki/Midpoint_circle_algorithm
**
****************************************************************************/
/*void HoughCircleDetector::draw_circle(QImage &image, const QPoint &position, unsigned int radius, const QColor &color)
{
  int f = 1 - radius;
  int ddF_x = 1;
  int ddF_y = -2 * radius;
  int x = 0;
  int y = radius;
  
  draw_pixel(image, QPoint(position.x(), position.y() + radius), color);
  draw_pixel(image, QPoint(position.x(), position.y() - radius), color);
  draw_pixel(image, QPoint(position.x() + radius, position.y()), color);
  draw_pixel(image, QPoint(position.x() - radius, position.y()), color);
  
  while(x < y)
  {
    if(f >= 0)
    {
      y--;
      ddF_y += 2;
      f += ddF_y;
    }
    
    x++;
    ddF_x += 2;
    f += ddF_x;
    
    draw_pixel(image, QPoint(position.x() + x, position.y() + y), color);
    draw_pixel(image, QPoint(position.x() - x, position.y() + y), color);
    draw_pixel(image, QPoint(position.x() + x, position.y() - y), color);
    draw_pixel(image, QPoint(position.x() - x, position.y() - y), color);
    draw_pixel(image, QPoint(position.x() + y, position.y() + x), color);
    draw_pixel(image, QPoint(position.x() - y, position.y() + x), color);
    draw_pixel(image, QPoint(position.x() + y, position.y() - x), color);
    draw_pixel(image, QPoint(position.x() - y, position.y() - x), color);
  }
}
*/
/****************************************************************************
**
** Author: Marc Bowes
**
** Draws at the specified position
**
****************************************************************************/
/*void HoughCircleDetector::draw_pixel(QImage &image, const QPoint &position, const QColor &color)
{
*/  /* bounds checking */
/*  if(position.x() < 0 || position.x() >= image.width() ||
     position.y() < 0 || position.y() >= image.height())
    {
    return;
  }
  
  image.setPixel(position, color.rgb());
}
*/
/****************************************************************************
**
** Author: Marc Bowes
**
** Detects edges in the specified QImage
**
****************************************************************************/
Mat CircleDetectorHough::edges(Mat src)
{

  Mat src_gray, grad, binary;

  if(!src.data)
  { 
    return 0; 
  }

  // Create container binary
  binary = Mat(src.rows, src.cols, CV_8UC1, 0.0);

  /// Create the kernel to the convolution 
  int valuesGx[9] = {1, 0, -1, 2, 0, -2, 1, 0, -1};
  int valuesGy[9] = {1, 2, 1, 0, 0, 0, -1, -2, -1};
  Mat Gx = Mat(3, 3, CV_32F, valuesGx); // to detect horizontal changes
  Mat Gy = Mat(3, 3, CV_32F, valuesGy); // to detect vertical changes

  cvtColor(src, src_gray, CV_BGR2GRAY);
  uint8_t *myData = src_gray.data;
  int width = src_gray.cols;
  int height = src_gray.rows;

  // to the source Mat
  for (int i = 0; i < width; i++)
  {
    for (int j = 0; j < height; j++)
    {
      double new_x = 0, new_y = 0;

      // gradient
      for (int k = -1; k <= 1; k++)
      {
        for (int z = -1; z <= 1; z++)
        {
          // values x,y to matrix source
          int x = i + k;
          int y = j + z;

          if (x < 0)  x = -x;
          else if (x >= width)  x = 2 * width - x - 2;

          if (y < 0)  y = -y;
          else if (y >= height) y = 2 * height - y - 2;

          int grayPixel = myData[(y * width) + x];
          new_x += Gx.at<int>(k + 1, z + 1) * grayPixel;
          new_y += Gy.at<int>(k + 1, z + 1) * grayPixel;
        }
      }

      int binaryPixel = sqrt(pow(new_x, 2) + pow(new_y, 2)) > 128 ? 1: 0;
      binary.at<int>(i,j) = binaryPixel;
      printf("(%i,%i) %i\n", i, j, binaryPixel);
    }
  }

  return binary;   
}