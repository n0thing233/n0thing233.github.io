#还行还行，一个visited的小bug.
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set((0,0))
        directions = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
        def go_back(robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        def helper(robot,row,col,direction):
            robot.clean()
            for i in range(4):
                new_dir = (direction+i)%4
                x = row + directions[new_dir][0]
                y = col + directions[new_dir][1]
                if (x,y) in cleaned or not robot.move():
                    robot.turnRight()
                    continue
                cleaned.add((x,y))
                helper(robot,x,y,new_dir)
                robot.turnRight()
            go_back(robot)
            return                
        helper(robot,0,0,0)
        return
