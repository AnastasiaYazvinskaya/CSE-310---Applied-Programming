package Snake;

/*
import java.awt.Graphics;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
*/
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;
import javax.swing.JPanel;

public class GamePanel extends JPanel implements ActionListener {
    
    static final int SCREEN_WIDTH = 600;
    static final int SCREEN_HEIGHT = 600;
    static final int UNIT_SIZE = 25; //Size of object in the game
    static final int GAME_UNITS = (SCREEN_WIDTH*SCREEN_HEIGHT)/UNIT_SIZE;
    static final int DELAY = 100;
    final int x[] = new int[GAME_UNITS];
    final int y[] = new int[GAME_UNITS];
    int bodyParts = 6; // Snake body at the start
    int fruitsEaten;
    int fruitX;
    int fruitY;
    Color fruitColor;
    char direction = 'R';
    boolean running = false;
    Timer timer;
    Random random;

    GamePanel(){
        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.black);
        this.setFocusable(true);
        this.addKeyListener(new MyKeyAdapter());
        startGame();
    }
    public void startGame(){
        /*
         * Create new fruit, start running and timer.
         */
        newFruit();
        running = true;
        timer = new Timer(DELAY, this);
        timer.start();
    }
    public void paintComponent(Graphics g){
        /*
         * 
         */
        super.paintComponent(g);
        draw(g);

    }
    public void draw(Graphics g){
        /*
         * 
         */
        // Draw grid
        if(running){
            for (int i=0; i < SCREEN_HEIGHT/UNIT_SIZE; i++){
                //Vertical lines
                g.drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);
                //Horizontal lines
                g.drawLine(0, i*UNIT_SIZE, SCREEN_WIDTH, i*UNIT_SIZE);
            }
            // Draw fruit
            //g.setColor(Color.red);
            g.setColor(fruitColor);
            g.fillOval(fruitX, fruitY, UNIT_SIZE, UNIT_SIZE);
            // Draw snake
            for(int i = 0; i<bodyParts; i++){
                if(i == 0){
                    g.setColor(Color.green);
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                }
                else {
                    g.setColor(new Color(45,180,0));
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                }
            }
            // Draw score
            g.setColor(Color.red);
            g.setFont(new Font("Ink Free", Font.BOLD, 40));
            FontMetrics metrics = getFontMetrics(g.getFont());
            g.drawString("Score: "+fruitsEaten, (SCREEN_WIDTH - metrics.stringWidth("Score: "+fruitsEaten))/2, g.getFont().getSize());
        }
        else{
            gameOver(g);
        }

    }
    public void newFruit(){
        /*
         * Set random coordinates for new fruit
         */
        fruitX = random.nextInt((int)(SCREEN_WIDTH/UNIT_SIZE))*UNIT_SIZE;
        fruitY = random.nextInt((int)(SCREEN_HEIGHT/UNIT_SIZE))*UNIT_SIZE;
        fruitColor = new Color(random.nextInt(255), random.nextInt(255), random.nextInt(255));
    }
    public void move(){
        /*
         * 
         */
        for(int i = bodyParts; i > 0; i--){
            x[i] = x[i-1];
            y[i] = y[i-1];
        }

        switch(direction){
            case 'U': //Up
                y[0] = y[0] - UNIT_SIZE;
                break;
            case 'D': //Down
                y[0] = y[0] + UNIT_SIZE;
                break;
            case 'L': //Left
                x[0] = x[0] - UNIT_SIZE;
                break;
            case 'R': //Right
                x[0] = x[0] + UNIT_SIZE;
                break;
        }
    }
    public void checkFruit(){
        if((x[0] == fruitX) && (y[0] == fruitY)){
            bodyParts++;
            fruitsEaten++;
            newFruit();
        }
    }
    public void checkCollisions(){
        // Check if head collides with body
        for(int i = bodyParts; i>0; i--){
            if((x[0] == x[i]) && (y[0] == y[i])){
                running = false;
            }
        }
        // Check if head out left
        if(x[0] < 0){
            running = false;
        }
        // Check if head out right
        if(x[0] > SCREEN_WIDTH){
            running = false;
        }
        // Check if head out top
        if(y[0] < 0){
            running = false;
        }
        // Check if head out bottom
        if(y[0] > SCREEN_HEIGHT){
            running = false;
        }

        if(!running){
            timer.stop();
        }

    }
    public void gameOver(Graphics g){
        // Score
        g.setColor(Color.red);
        g.setFont(new Font("Ink Free", Font.BOLD, 40));
        FontMetrics metrics1 = getFontMetrics(g.getFont());
        g.drawString("Score: "+fruitsEaten, (SCREEN_WIDTH - metrics1.stringWidth("Score: "+fruitsEaten))/2, g.getFont().getSize());
        // Game Over text
        g.setColor(Color.red);
        g.setFont(new Font("Ink Free", Font.BOLD, 75));
        FontMetrics metrics2 = getFontMetrics(g.getFont());
        g.drawString("Game Over", (SCREEN_WIDTH - metrics2.stringWidth("Game Over"))/2, SCREEN_HEIGHT/2);
    }

    @Override
    public void actionPerformed(ActionEvent e){
        if(running){
            move();
            checkFruit();
            checkCollisions();
        }
        repaint();

    }

    public class MyKeyAdapter extends KeyAdapter{
        @Override
        public void keyPressed(KeyEvent e){
            /*
             * Chech pressed key and change direction if needed.
             */
            switch(e.getKeyCode()){
                case KeyEvent.VK_LEFT:
                    if(direction != 'R'){
                        direction = 'L';
                    }
                    break;
                case KeyEvent.VK_RIGHT:
                    if(direction != 'L'){
                        direction = 'R';
                    }
                    break;
                case KeyEvent.VK_UP:
                    if(direction != 'D'){
                        direction = 'U';
                    }
                    break;
                case KeyEvent.VK_DOWN:
                    if(direction != 'U'){
                        direction = 'D';
                    }
                    break;
            }
            
        }
    }
}
