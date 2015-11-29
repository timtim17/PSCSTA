package me.timtim17.dev.pscsta.spring2015.java.test;

import me.timtim17.dev.pscsta.spring2015.java.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;

public class ProblemTestsStudentData {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUpStreams() {
        System.setOut(null);
    }

    @Test
    public void testPracticeProblem() {
        PracticeProblem.main(new String[] {});
        assertOutput(new String[] {"Let's play Checkers!", "Let's play Hide and Go Seek!", "Let's play Battleship!"});
    }

    @Test
    public void testDetermined1() throws Exception {
        Determined1.main(new String[] {});
        assertOutput(new String[] {"-3", "0", "22"});
    }

    @Test
    public void testBankStreetWriter() throws Exception {
        BankStreetWriter.main(new String[] {});
        assertOutput(new String[] {"16", "I LIKE DOING THOSE PROBLEMS", "I LIKE THESE PROBLEMS", "I LIKE DOING THESE CSTA PROBLEMS", "WHY DO I LIKE DOING THESE CSTA PROBLEMS"});
    }

    @Test
    public void testSplatter() throws Exception {
        Splatter.main(new String[] {});
        assertOutput(new String[] {"NO", "YES"});
    }

    @Test
    public void testDrought() throws Exception {
        Drought.main(new String[] {});
        assertOutput(new String[] {"continuing", "improving", "drought over"});
    }

    @Test
    public void testCross() throws Exception {
        Cross.main(new String[] {});
        assertOutput(new String[] {" g", "cross", " e", " e", " n", "", "      d", "      o", "playing", "", "none", "", "   l", "school", "   v", "   e", ""});
    }

    @Test
    public void testBuoyancy() throws Exception {
        Buoyancy.main(new String[] {});
        assertOutput(new String[] {"50", "10", "9"});
    }

    @Test
    public void testAccounting() throws Exception {
        Accounting.main(new String[] {});
        assertOutput(new String[] {"****.****.****.****.****.****.****.****.", "       Transaction : Balance","           $250.34 : $250.34", "         $(500.19) : $(249.85)", "     $2,343,555.55 : $2,343,305.70", "      $(59,216.99) : $2,284,088.71", "****.****.****.****.****.****.****.****."});
    }

    @Test
    public void testCursed() throws Exception {
        Cursed.main(new String[] {});
        assertOutput(new String[] {"06011998: OK TO TRAVEL", "01090109: OK TO TRAVEL", "12311321: DON'T TRAVEL"});
    }

    @Test
    public void testDataCount() throws Exception {
        DataCount.main(new String[] {});
        assertOutput(new String[] {"THERE ARE 73 LINES OF DATA FOR THIS PACKET"});
    }

    @Test
    public void testHistoNum() throws Exception {
        HistoNum.main(new String[] {});
        assertOutput(new String[] {"0|** {2}", "1|** {2}", "2|**** {4}", "3|***** {5}", "5|*** {3}", "6|* {1}", "7|*** {3}", "8|**** {4}", "9|*** {3}"});
    }

    @Test
    public void testSayHello() {
        SayHello.main(new String[] {});
        assertOutput(new String[] {"Hello judges! Our names are Austin, Myself, and I. There are 13 letters in our names. Have a wolf strong day! Wolf Strong Pack Strong!"});
    }

    @Test
    public void testShuffle() throws Exception {
        Shuffle.main(new String[] {});
        assertOutput(new String[] {"ALPHABETICAL IN ONLY ORDER PRINT THE UNIQUE WORDS ", "ALL BELLS JINGLE THE WAY ", "AND DOES EAT IVY LAMBS LITTLE MARES OATS ", "ON SEASHELLS SEASHORE SELLS SHE THE ", "HELLO WORLD "});
    }

    @Test
    public void testSineUp() throws Exception {
        SineUp.main(new String[] {});
        assertOutput(new String[] {"Circumcircle diameter = 100", "Angles are 40, 60 and 80", "Corresponding sides are 64, 87 and 98", "Circumcircle diameter = 50", "Angles are 45, 45 and 90", "Corresponding sides are 35, 35 and 50", "Circumcircle diameter = 70", "Angles are 90, 60 and 30", "Corresponding sides are 70, 61 and 35"});
    }

    @Test
    public void testDetermined2() throws Exception {
        Determined2.main(new String[] {});
        assertOutput(new String[] {"2", "2", "408"});
    }

    private void assertOutput(String[] expected) {
        assertEquals(String.join("\r\n", expected) + "\r\n", outContent.toString());
    }
}