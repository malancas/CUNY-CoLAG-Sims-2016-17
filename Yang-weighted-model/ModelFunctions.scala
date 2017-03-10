package modelfunctions

class ModelFunctions {
  def makeGrammarGo(i: Int, weights: List[Double], grammar: List[Int]): List[Int] =
    if (i == 14) grammar
    else {
      weights match {
        case h :: t =>
          if(h >= 0.5) makeGrammarGo(i+1, t, grammar :+ 1)
          else makeGrammarGo(i+1, t, grammar :+ 0)
        
        case nil => grammar
      }
    }

  def makeGrammar(weights: List[Double]): List[Int] =
    makeGrammarGo(1, weights, List())

  def updateWeights(weights: List[Double], grammar: List[Int], parsed: Boolean, newWeights: List[Double]): List[Double] =
    weights match {
      case h :: t =>
        if ((parsed && grammar.head == 1) || (!parsed && grammar.head == 0)) updateWeights(t, grammar.tail, parsed, newWeights :+ (h + 0.1))
        else if ((parsed && grammar.head == 0) || (!parsed && grammar.head == 1)) updateWeights(t, grammar.tail, parsed, newWeights :+ (h - 0.1))

        else {
          println("Should never reach here")
          List()
        }
      case nil => newWeights
    }

  // Implementing LRP-scheme: https://books.google.com/books?id=-zdWJ9Adp1wC&pg=PA110&lpg=PA110&dq=linear+reward+penalty+scheme+bush&source=bl&ots=u6IsuDpd5y&sig=CVtmdd6SYgtni3nQj2yDx-phZoI&hl=en&sa=X&ved=0ahUKEwiO8sHb0MrSAhVEzIMKHRPCDZMQ6AEIKzAD#v=onepage&q=linear%20reward%20penalty%20scheme%20bush&f=false


  /*
  def processSentences(i: Int, weights: List[Int], targetSentences: Array[List[String]]): List[Int] =
    if (i == args(0)) weights
    else {
      currSentence = targetSentences(Random.nextInt(targetSentences.size))
      currGrammar = makeGrammar(weights)
      if (currSentence(0).toInt == Integer.parseInt(currGrammar.mkString(""),2)) println(Success)
      what(i+1, grammar, weights, targetSentences)
    }

  def rewardGrammar(grammar: List[Int], weights: Array[Double]): Array[Double] =
    def go(i: Int, grammar: List[Int], weights: Array[Double]): Array[Double] =
      if (i == 14) weights
      else {
        println("Hey")
      }
 */
}
   
