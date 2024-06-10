package pt.ulusofona.lp2.deisichess;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class GameManager {

int boardSize = 0;
Peca[][] tabuleiro;
HashMap<Integer,Peca> conjuntoDePecas;
int numPecas = 0;
int currentTeam = 0;
GameResults gameResults = new GameResults();



    boolean loadFile(File file){
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));

            boardSize = Integer.parseInt(reader.readLine().trim());
            numPecas = Integer.parseInt(reader.readLine().trim());
            conjuntoDePecas = new HashMap<>();

            for (int i = 0; i < numPecas; i++) {
                String pecaInformacao = reader.readLine().trim();
                String[] parts = pecaInformacao.split(":");
                int id = Integer.parseInt(parts[0]);
                int type = Integer.parseInt(parts[1]);
                int teamId = Integer.parseInt(parts[2]);
                String name = parts[3];

                Peca peca = new Peca(id,type,teamId,name);
                conjuntoDePecas.put(id,peca);
            }

            Peca[][] tabuleiroTemp = new Peca[boardSize][boardSize];

            for (int i = 0; i < boardSize; i++) {
                String[] rowInfo = reader.readLine().trim().split(":");
                if(rowInfo.length==boardSize-1){
                    for (int j = 0; j < rowInfo.length; j++) {
                        int position = Integer.parseInt(rowInfo[j]);
                        if(position != 0){
                            tabuleiroTemp[i][j] = conjuntoDePecas.get(position);
                        }
                    }
                }else{
                    reader.close();
                    return false;
                }
            }
            tabuleiro = tabuleiroTemp;
            reader.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    int getBoardSize(){
        return boardSize;
    }



    String getPieceInfoAsString(int ID){
        if(!conjuntoDePecas.containsKey(ID)){
            return null;
        }
        return conjuntoDePecas.get(ID).toString();
    }

    int getCurrentTeamID(){
        return currentTeam;
    }

    ArrayList<String> getGameResults(){
        ArrayList<String> temp = new ArrayList<>();
        temp.add("JOGO DE CRAZY CHESS");
        temp.add("Resultado: "+gameResults.getResultado());
        temp.add("---");
        temp.add("Equipa das Pretas");
        temp.add(Integer.toString(gameResults.getNumCapturadasPretas()));
        temp.add(Integer.toString(gameResults.getNumJogadasValPretas()));
        temp.add(Integer.toString(gameResults.getNumJogadasInvPretas()));
        temp.add("Equipa das Brancas");
        temp.add(Integer.toString(gameResults.getNumCapturadasBrancas()));
        temp.add(Integer.toString(gameResults.getNumJogadasValBrancas()));
        temp.add(Integer.toString(gameResults.getNumJogadasInvBrancas()));
        return temp;
    }








}
