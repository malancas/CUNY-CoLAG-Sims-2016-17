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

    // Set up initial weights
    val weights = List.fill(13)(0.5)

    val grammar = new ModelFunctions makeGrammar(weights)
    println(grammar)

    val newWeights = new ModelFunctions updateWeights(weights, grammar, true, List())
    println(newWeights)
  }
}
