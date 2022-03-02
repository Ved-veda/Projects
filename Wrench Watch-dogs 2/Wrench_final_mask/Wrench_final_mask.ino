// Full mask with two max7219 and led matrices for both sides.
#include <LedControl.h>
int DIN1 = 10;  // right one
int CS1  = 9;   
int CLK1 = 8;

int DIN2 = 7; // left one
int CS2  = 6;
int CLK2 = 5;

LedControl lc1 = LedControl(DIN1,CLK1,CS1,1);
LedControl lc2 = LedControl(DIN2,CLK2,CS2,1);

void setup() 
{
  lc1.shutdown(0,false);
  lc2.shutdown(0,false);

  lc1.setIntensity(0,4);
  lc2.setIntensity(0,4);

  lc1.clearDisplay(0);
  lc2.clearDisplay(0);
}

void loop() 
{
//common ones  
    byte wx[8] = {0xC1,0x63,0x36,0x1C,0x38,0x6C,0xC6,0x83};
    byte hash[8] = {0x6C,0x6C,0xFF,0x6C,0x6C,0xFF,0x6C,0x6C};
    byte zed[8] = {0xFF,0x7F,0x0E,0x1C,0x38,0x70,0xFE,0xFF};

    printByte(wx);
    delay(3000);
    printByte(hash);
    delay(3000);    
    printByte(zed);
    delay(3000);

//LEFT EYE
    byte atrateleft[8] = {0x7C,0x02,0x39,0x55,0x55,0x59,0x42,0x3C};
    byte winkleftpart[8] = {0x00,0x30,0x79,0xFB,0xDF,0x8E,0x00,0x00};
    byte leftcircle[8] = {0x30,0x48,0x84,0x84,0x84,0x84,0x48,0x30};
    byte sadleft[8] = {0x00,0x06,0x0E,0x1C,0x38,0x70,0x60,0x00};
    byte angryleft[8] = {0x00,0x60,0x70,0x38,0x1C,0x0E,0x06,0x00}; 
   
    byte nineleft[8] = {0x38,0x44,0x40,0x40,0x78,0x44,0x44,0x38};
    byte questionmarkleft[8] = {0x08,0x00,0x08,0x08,0x10,0x26,0x22,0x1C};
    byte semicolonleft[8] = {0x04,0x0C,0x18,0x18,0x08,0x00,0x18,0x18};
    byte exclaimedleft[8] = {0x10,0x00,0x10,0x38,0x38,0x38,0x38,0x10};

//RIGHT EYE
    byte atrateright[8] = {0x3C,0x42,0x99,0xA5,0xAA,0x9C,0x41,0x3E};
    byte winkrightpart[8] = {0x18,0x3C,0x7E,0xFF,0xE7,0xC3,0x81,0x00};
    byte smallercircle[8] = {0x00,0x0C,0x12,0x12,0x12,0x0C,0x00,0x00};
    byte sadright[8] = {0x00,0x60,0x70,0x38,0x1C,0x0E,0x06,0x00};
    byte angryright[8] = {0x00,0x06,0x0E,0x1C,0x38,0x70,0x60,0x00};
  
    byte nineright[8] = {0x1C,0x22,0x22,0x22,0x1E,0x02,0x22,0x1C};
    byte questionmarkright[8] = {0x38,0x44,0x64,0x08,0x10,0x10,0x00,0x10};
    byte semicolonright[8] = {0x18,0x18,0x00,0x18,0x0C,0x0C,0x08,0x10};
    byte exclaimedright[8] = {0x08,0x1C,0x1C,0x1C,0x1C,0x08,0x00,0x08};
    
//Excecute together
    printByteleft2(winkleftpart);
    printByteright1(winkrightpart);
    delay(3000);

    printByteleft2(leftcircle);
    printByteright1(smallercircle);
    delay(3000);

    printByteleft2(sadleft);
    printByteright1(sadright);
    delay(3000);

    printByteleft2(angryleft);
    printByteright1(angryright);
    delay(3000);

  

    printByteleft2(nineleft);
    printByteright1(nineright);
    delay(3000);

    printByteleft2(questionmarkleft);
    printByteright1(questionmarkright);
    delay(3000);

    printByteleft2(semicolonleft);
    printByteright1(semicolonright);
    delay(3000);

    printByteleft2(exclaimedleft);
    printByteright1(exclaimedright);
    delay(3000);
    
}


void printByte(byte character [])
{int i = 0;
 for(i=0;i<8;i++)
 {lc1.setRow(0,i,character[i]);
  lc2.setRow(0,i,character[i]);
  }
}


void printByteright1(byte character [])
{int i = 0;
 for(i=0;i<8;i++)
  {lc1.setRow(0,i,character[i]);}
}

void printByteleft2(byte character [])
{int i = 0;
 for(i=0;i<8;i++)
  {lc2.setRow(0,i,character[i]);}
}