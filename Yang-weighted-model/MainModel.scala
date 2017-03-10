import scala.io.Source
import scala.util.Random
import modelfunctions.ModelFunctions

object MainModel {
  val usage = """
    Usage: mmlaln [Number of input sentences] [Target grammar code (French=584, English=611, German=2253, Japanese=3856)]
  """
  def main(args: Array[String]): Unit = {
    if (args.length != 2){
      println(usage)
      return
    }

    // Read target language sentences from EngFrJapGerm.txt
    val targetSentences = io.Source.fromFile("../EngFrJapGerm.txt").getLines.map(x => x.split('\t')).filter(line =>line(0) == args(1)).toArray
    //println(targetSentences.deep.mkString("\n"))

    // Create initial weights and grammar lists
    val weights = List.fill(13)(0.5)
    val grammar = List(0,0,0,0,0,0,1,0,0,0,1,0,1)

    val newWeights = new ModelFunctions updateWeights(weights, grammar, false, List())
    println(newWeights)
    val newGrammar = new ModelFunctions makeGrammar(newWeights)
    println(newGrammar)
  }
}
