/*
 *    SPDX-FileCopyrightText: 2021 Monaco F. J. <monaco@usp.br>
 *    SPDX-FileCopyrightText: 2024 joaovta <joaovta7@gmail.com>
 *   
 *    SPDX-License-Identifier: GPL-3.0-or-later
 *
 *  This file is a derivative work from SYSeg (https://gitlab.com/monaco/syseg)
 *  and contains modifications carried out by the following author(s):
 *  joaovta <joaovta7@gmail.com>
 */

#include "bios.h"
#include "opt.h"

#define PROMPT "$ "		/* Prompt sign.      */
#define SIZE 20			/* Read buffer size. */

#define EYES_OPEN "(o_o)"		
#define EYES_CLOSED "(>_<)"		

char buffer[SIZE];		/* Read buffer.      */

int main()
{
  clear();
  println  ("Boot Command 1.0");
  while (1)
  {
    print(PROMPT);		/* Show prompt.               */
    readln(buffer);		/* Read use input.            */

    if (buffer[0])		/* Execute built-in command.  */
    {
      if (!strcmp(buffer,"help"))
      {
        println("A Beattles's song.");
      }
      else if (!strcmp(buffer,"sup"))
      {
        int a = 0;
        clear();
        println(EYES_OPEN);
        for(int i = 0; i < 1000000; i++) {
          a = i + a;
        }
        clear();
        println(EYES_CLOSED);
      }
      else{
        println("Unkown command.");
      }
    }
  }
  return 0;
}

