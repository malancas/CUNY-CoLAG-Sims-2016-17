import collection.mutable.Stack
import ModelFunctions.reward
import org.scalatest._

class RewardSpec extends FlatSpec with Matchers {
  "reward" should "return a new weight" in {
    assert(reward(0.5, 0.5) == 0.75)
    assert(reward(0.1, 0.5) == 0.55)
  }
}
