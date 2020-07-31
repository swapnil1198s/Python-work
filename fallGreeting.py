# Name: Swapnil Srivastava

# fallGreeting.py

# Problem: this program displays a fallgreeting card
#               with flickering jack-o-lantern light.

# Certification of Authenticity:

# I certify that this lab is entirely my own work.

from graphics import *

def fallGreeting():

#set dimensions of the window and set the background color
    win = GraphWin("fallGreeting", 800, 600)
    win.setBackground("Midnight Blue")

#Create the ground
    ground = Polygon(Point( 0 , 474 ), Point( 9 , 474 ),
                     Point( 20 , 474 ), Point( 32 , 474 ),
                     Point( 45 , 475 )
                     , Point( 54 , 475 ), Point( 64 , 476 ),
                     Point( 75 , 476 ), Point( 84 , 475 ),
                     Point( 93 , 475 )
                     , Point( 103 , 474 ), Point( 111 , 472 ),
                     Point( 130 , 472 ), Point( 142 , 472 )
                     , Point( 159 , 473 ), Point( 174 , 476 ),
                     Point( 189 , 478 ), Point( 199 , 477 )
                     , Point( 222 , 477 ), Point( 232 , 476 ),
                     Point( 248 , 475 ), Point( 271 , 474 )
                     , Point( 285 , 474 ), Point( 297 , 476 ),
                     Point( 317 , 476 ), Point( 326 , 476 )
                     , Point( 339 , 476 ), Point( 350 , 477 ),
                     Point( 355 , 476 ), Point( 372 , 476 )
                     , Point( 391 , 476 ), Point( 403 , 475 ),
                     Point( 419 , 474 ), Point( 428 , 474 )
                     , Point( 436 , 474 ), Point( 444 , 472 ),
                     Point( 451 , 471 ), Point( 462 , 471 )
                     , Point( 468 , 471 ), Point( 477 , 471 ),
                     Point( 484 , 471 ), Point( 493 , 472 )
                     , Point( 519 , 474 ), Point( 532 , 475 ),
                     Point( 543 , 474 ), Point( 558 , 473 )
                     , Point( 574 , 473 ), Point( 586 , 471 ),
                     Point( 604 , 474 ), Point( 615 , 474 )
                     , Point( 633 , 475 ), Point( 654 , 477 ),
                     Point( 667 , 477 ), Point( 686 , 476 )
                     , Point( 704 , 478 ),Point( 713 , 477 ),
                     Point( 723 , 479 ), Point( 730 , 480 )
                     , Point( 739 , 479 ), Point( 747 , 480 ),
                     Point( 755 , 480 ), Point( 763 , 478 )
                     , Point( 769 , 476 ), Point( 771 , 476 ),
                     Point( 774 , 474 ), Point( 776 , 474)
                     , Point( 783 , 471 ), Point( 786 , 469 ),
                     Point( 788 , 469 ), Point( 792 , 468 )
                     , Point( 796 , 467 ), Point( 799 , 467 ),
                     Point( 803 , 467 ), Point(800, 600), Point(0, 600))

#Color the ground
    ground.setFill("Brown")

#Create the jack-o-lantern
    jack = Polygon(Point( 437 , 484 ), Point( 433 , 486 ),
                   Point( 427 , 489 ), Point( 422 , 491 ),
                   Point( 414 , 494 ), Point( 409 , 496 ),
                   Point( 404 , 496 ), Point( 396 , 497 ),
                   Point( 386 , 498 ), Point( 379 , 498 ),
                   Point( 371 , 498 ), Point( 361 , 498 ),
                   Point( 354 , 498 ), Point( 347 , 498 ),
                   Point( 336 , 494 ), Point( 325 , 491 ),
                   Point( 315 , 486 ), Point( 309 , 481 ),
                   Point( 304 , 476 ), Point( 297 , 470 ),
                   Point( 292 , 464 ), Point( 285 , 456 ),
                   Point( 282 , 452 ), Point( 280 , 447 ),
                   Point( 278 , 443 ), Point( 275 , 439 ),
                   Point( 273 , 434 ), Point( 272 , 428 ),
                   Point( 269 , 422 ), Point( 267 , 415 ),
                   Point( 268 , 407 ), Point( 265 , 399 ),
                   Point( 266 , 389 ), Point( 266 , 382 ),
                   Point( 269 , 374 ), Point( 270 , 366 ),
                   Point( 272 , 356 ), Point( 277 , 348 ),
                   Point( 280 , 340 ), Point( 284 , 333 ),
                   Point( 289 , 327 ), Point( 293 , 322 ),
                   Point( 297 , 318 ), Point( 304 , 315 ),
                   Point( 310 , 314 ), Point( 318 , 312 ),
                   Point( 326 , 309 ), Point( 333 , 308 ),
                   Point( 343 , 307 ), Point( 351 , 306 ),
                   Point( 361 , 304 ), Point( 368 , 303 ),
                   Point( 377 , 301 ), Point( 387 , 301 ),
                   Point( 393 , 302 ), Point( 399 , 302 ),
                   Point( 410 , 302 ), Point( 418 , 303 ),
                   Point( 425 , 304 ), Point( 433 , 306 ),
                   Point( 442 , 309 ), Point( 451 , 314 ),
                   Point( 458 , 321 ), Point( 465 , 329 ),
                   Point( 470 , 337 ), Point( 474 , 343 ),
                   Point( 479 , 354 ), Point( 482 , 364 ),
                   Point( 484 , 375 ), Point( 485 , 388 ),
                   Point( 485 , 397 ), Point( 485 , 405 ),
                   Point( 483 , 413 ), Point( 483 , 419 ),
                   Point( 481 , 426 ), Point( 479 , 432 ),
                   Point( 475 , 438 ), Point( 473 , 444 ),
                   Point( 471 , 450 ), Point( 468 , 454 ),
                   Point( 464 , 457 ), Point( 461 , 462 ),
                   Point( 456 , 467 ), Point( 452 , 470 ),
                   Point( 445 , 476 ), Point( 441 , 480 ),
                   Point( 436 , 483 ))
    
#color the jack-o-lantern
    jack.setFill("Orange Red")

#create the stem of jack-o-lantern
    jackStem = Polygon(Point( 359 , 302 ), Point( 361 , 299 ),
                    Point( 361 , 293 ), Point( 360 , 284 ),
                    Point( 357 , 275 ), Point( 354 , 271 ),
                    Point( 359 , 268 ), Point( 362 , 267 ),
                    Point( 367 , 272 ), Point( 369 , 278 ),
                    Point( 371 , 283 ), Point( 371 , 289 ),
                    Point( 373 , 294 ), Point( 371 , 299 ),
                    Point( 370 , 302 ))
#draw the lantern
    jackStem.draw(win)
#color the lantern
    jackStem.setFill("green")

#create the left eye for the lantern
    jackEye1 = Polygon(Point( 337 , 348 ), Point( 333 , 354 ),
                       Point( 328 , 361 ), Point( 323 , 368 ),
                       Point( 319 , 374 ), Point( 316 , 381 ),
                       Point( 314 , 390 ), Point( 315 , 399 ),
                       Point( 321 , 401 ), Point( 328 , 404 ),
                       Point( 338 , 405 ), Point( 348 , 398 ),
                       Point( 351 , 389 ), Point( 355 , 377 ),
                       Point( 356 , 364 ), Point( 356 , 356 ),
                       Point( 355 , 350 ), Point( 353 , 343 ),
                       Point( 348 , 341 ), Point( 344 , 341 ),
                       Point( 341 , 347 ))
    
    
#create the right eye for the lantern
    jackEye2 = Polygon(Point( 394 , 340 ),
                       Point( 393 , 346 ),
                       Point( 394 , 355 ),
                       Point( 397 , 367 ),
                       Point( 400 , 378 ),
                       Point( 404 , 385 ),
                       Point( 407 , 394 ),
                       Point( 414 , 397 ),
                       Point( 420 , 397 ),
                       Point( 430 , 392 ),
                       Point( 433 , 386 ),
                       Point( 432 , 374 ),
                       Point( 429 , 362 ),
                       Point( 427 , 357 ),
                       Point( 423 , 350 ),
                       Point( 421 , 347 ),
                       Point( 417 , 343 ),
                       Point( 413 , 339 ), Point( 408 , 334 ),
                       Point( 405 , 334 ), Point( 401 , 334 ),
                       Point( 398 , 334 ), Point( 397 , 337 ))
  

#create the left nostril for the lantern
    jackNose1 = Polygon(Point( 367 , 401 ), Point( 365 , 406 ),
                        Point( 362 , 411 ), Point( 362 , 414 ),
                        Point( 364 , 417 ), Point( 367 , 417 ),
                        Point( 370 , 415 ), Point( 372 , 410 ),
                        Point( 373 , 405 ), Point( 373 , 401 ),
                        Point( 369 , 400 ))
    
#create the right nostril for the lantern
    jackNose2 = Polygon(Point( 379 , 401 ), Point( 380 , 405 ),
                        Point( 380 , 408 ), Point( 381 , 411 ),
                        Point( 383 , 415 ), Point( 386 , 415 ),
                        Point( 389 , 414 ), Point( 390 , 411 ),
                        Point( 388 , 406 ), Point( 386 , 403 ),
                        Point( 385 , 401 ), Point( 382 , 400 ))

#create the mouth for jack-o-lantern
    jackMouth = Polygon(Point( 285 , 414 ), Point( 296 , 424 ),
                        Point( 310 , 432 ), Point( 322 , 437 ),
                        Point( 336 , 440 ), Point( 350 , 442 ),
                        Point( 358 , 451 ), Point( 369 , 451 ),
                        Point( 374 , 441 ), Point( 388 , 441 ),
                        Point( 396 , 442 ), Point( 402 , 450 ),
                        Point( 412 , 450 ), Point( 415 , 441 ),
                        Point( 422 , 438 ), Point( 430 , 433 ),
                        Point( 441 , 427 ), Point( 448 , 419 ),
                        Point( 454 , 411 ), Point( 461 , 403 ),
                        Point( 464 , 411 ), Point( 460 , 419 ),
                        Point( 455 , 432 ), Point( 446 , 445 ),
                        Point( 433 , 455 ), Point( 414 , 467 ),
                        Point( 401 , 472 ), Point( 394 , 463 ),
                        Point( 378 , 462 ), Point( 369 , 472 ),
                        Point( 356 , 470 ), Point( 340 , 463 ),
                        Point( 328 , 458 ), Point( 319 , 452 ),
                        Point( 311 , 443 ), Point( 296 , 433 ))
    

#create the moon
    moon = Circle(Point(120, 110), 65)
#draw the moon
    moon.draw(win)
#color the moon
    moon.setFill("Gainsboro")

#create the tree
    tree = Polygon(Point( 801 , 466 ), Point( 796 , 466 ),
                   Point( 790 , 468 ), Point( 777 , 473 ),
                   Point( 771 , 475 ), Point( 760 , 477 ),
                   Point( 753 , 479 ), Point( 738 , 480 ),
                   Point( 729 , 480 ), Point( 720 , 478 ),
                   Point( 712 , 476 ), Point( 712 , 462 ),
                   Point( 713 , 452 ), Point( 715 , 441 ),
                   Point( 717 , 427 ), Point( 718 , 414 ),
                   Point( 719 , 397 ), Point( 722 , 370 ),
                   Point( 722 , 348 ), Point( 724 , 322 ),
                   Point( 724 , 299 ), Point( 723 , 286 ),
                   Point( 722 , 266 ), Point( 720 , 255 ),
                   Point( 713 , 245 ), Point( 707 , 232 ),
                   Point( 701 , 227 ), Point( 688 , 218 ),
                   Point( 669 , 212 ), Point( 656 , 209 ),
                   Point( 641 , 206 ), Point( 622 , 205 ),
                   Point( 612 , 207 ), Point( 596 , 210 ),
                   Point( 583 , 211 ), Point( 575 , 214 ),
                   Point( 579 , 208 ), Point( 584 , 201 ),
                   Point( 592 , 198 ), Point( 601 , 199 ),
                   Point( 606 , 194 ), Point( 604 , 188 ),
                   Point( 598 , 187 ), Point( 589 , 185 ),
                   Point( 583 , 190 ), Point( 578 , 192 ),
                   Point( 572 , 194 ), Point( 561 , 194 ),
                   Point( 551 , 193 ), Point( 540 , 192 ),
                   Point( 532 , 192 ), Point( 521 , 191 ),
                   Point( 514 , 190 ), Point( 509 , 193 ),
                   Point( 500 , 197 ), Point( 504 , 192 ),
                   Point( 510 , 184 ), Point( 521 , 182 ),
                   Point( 530 , 180 ), Point( 539 , 178 ),
                   Point( 546 , 179 ), Point( 560 , 183 ),
                   Point( 571 , 178 ), Point( 582 , 175 ),
                   Point( 590 , 174 ), Point( 602 , 175 ),
                   Point( 614 , 178 ), Point( 646 , 185 ),
                   Point( 655 , 184 ), Point( 666 , 183 ),
                   Point( 686 , 183 ), Point( 696 , 176 ),
                   Point( 708 , 166 ), Point( 717 , 158 ),
                   Point( 723 , 144 ), Point( 725 , 135 ),
                   Point( 727 , 123 ), Point( 728 , 107 ),
                   Point( 728 , 89 ), Point( 729 , 69 ),
                   Point( 728 , 51 ), Point( 727 , 29 ),
                   Point( 724 , 13 ), Point( 718 , 8 ),
                   Point( 708 , 1 ), Point(803, 0))

#draw the tree
    tree.draw(win)
#color the tree
    tree.setFill("black")

#create the tombstones for the background and draw them
    tombStone3 = Polygon(Point( 122 , 472 ), Point( 122 , 415 ),
                         Point( 126 , 411 ), Point( 132 , 408 ),
                         Point( 137 , 406 ), Point( 143 , 404 ),
                         Point( 153 , 403 ), Point( 162 , 405 ),
                         Point( 167 , 410 ), Point( 171 , 417 ),
                         Point( 171 , 424 ), Point( 172 , 476 ))
    tombStone3.draw(win)
    tombStone3.setFill("slate grey")

    tombStone1 = Polygon(Point( 44 , 476 ), Point( 46 , 410 ),
                         Point( 49 , 404 ), Point( 52 , 401 ),
                         Point( 56 , 396 ), Point( 64 , 395 ),
                         Point( 70 , 395 ), Point( 75 , 397 ),
                         Point( 78 , 400 ), Point( 80 , 405 ),
                         Point( 82 , 410 ), Point( 79 , 478 ))
    tombStone1.draw(win)
    tombStone1.setFill("slate grey")

    tombStone2 = Polygon(Point( 70 , 476 ), Point( 72 , 377 ),
                         Point( 78 , 370 ), Point( 83 , 366 ),
                         Point( 89 , 364 ), Point( 95 , 362 ),
                         Point( 104 , 362 ), Point( 111 , 362 ),
                         Point( 121 , 364 ), Point( 128 , 368 ),
                         Point( 132 , 374 ), Point( 134 , 382 ),
                         Point( 133 , 474 ))
    tombStone2.draw(win)
    tombStone2.setFill("slate grey")

    tombStone4 = Polygon(Point( 540 , 478 ), Point( 516 , 412 ),
                         Point( 514 , 405 ), Point( 514 , 400 ),
                         Point( 517 , 394 ), Point( 519 , 388 ),
                         Point( 526 , 384 ), Point( 534 , 383 ),
                         Point( 545 , 384 ), Point( 553 , 389 ),
                         Point( 560 , 397 ),  Point( 601 , 479 ))
    tombStone4.draw(win)
    tombStone4.setFill("slate grey")

    tombStone5 = Polygon(Point( 580 , 471 ), Point( 581 , 389 ),
                         Point( 585 , 383 ), Point( 589 , 378 ),
                         Point( 593 , 374 ), Point( 599 , 370 ),
                         Point( 607 , 368 ), Point( 614 , 367 ),
                         Point( 623 , 369 ), Point( 630 , 370 ),
                         Point( 634 , 375 ), Point( 640 , 380 ),
                         Point( 642 , 388 ), Point( 640 , 475 ))
    tombStone5.draw(win)
    tombStone5.setFill("slate grey")

    tombstoneText = Text(Point( 100 , 394 ), "R.I.P")
    
#draw dround and the jack-o-lantern in correct order
    ground.draw(win)
    jack.draw(win)
    jackMouth.draw(win)
    jackEye1.draw(win)
    jackEye2.draw(win)
    jackNose1.draw(win)
    jackNose2.draw(win)

#Create text "happy fall!" to be displayed in the background
    greeting = Text(Point( 381 , 100), "HAPPY FALL!")
    greeting.draw(win)
    greeting.setSize(36)
    greeting.setStyle("bold italic")
    greeting.setTextColor("Orange red")
#declare colors to be flashed inside the jack-o-lantern
    colors = ["Yellow", "black", "yellow", "black", "Yellow",
              "black", "yellow", "black", "Yellow", "black",
              "yellow", "black", "yellow"]

#write the loop for the flickering of light
    for color in colors:
        
        jackEye1.setFill(color)
        jackEye2.setFill(color)
        jackMouth.setFill(color)
        jackNose1.setFill(color)
        jackNose2.setFill(color)
        
        time.sleep(0.5)

#provide instruction for closing the window
    instructions = Text(Point(400,  570),
                        "Click anywhere to close.")
    instructions.setTextColor("White")


    instructions.draw(win)
# Wait for another click to exit
    win.getMouse()
    win.close()

def main():
    fallGreeting()

main()

