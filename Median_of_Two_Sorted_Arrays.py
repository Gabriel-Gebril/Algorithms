# Time complexity is O(log(min(x,y))
class Solution:
    def findMedianSortedArrays(self,nums1: List[int], nums2: List[int]) -> float:        
        if len(nums1) < len(nums2):
            x = len(nums1)
            xarr = nums1
            y = len(nums2)
            yarr = nums2
        else:
            x = len(nums2)
            xarr = nums2
            y = len(nums1)
            yarr = nums1
            
        if(x == 0 and y%2 == 0):
            return (yarr[y//2] + yarr[y//2-1])/2
        elif(x==0 and y%2 != 0):
            return yarr[y//2]
        
        if(y == 0 and x%2 == 0):
            return (xarr[x//2] + xarr[x//2-1])/2
        elif(y==0 and x%2 != 0):
            return xarr[x//2]
        
            
        # x is the smaller array, y is the bigger array.
        px = x//2
        
        py = ((x + y + 1)//2) - px
        #print(px,py)

        if (px >= x):
            xrs = 1000000000000000000000000
            xls = xarr[x-1]
        elif (px <= 0):
            xls = -1000000000000000000000000
            xrs = xarr[0]
        else:
            xls = xarr[px-1]
            xrs = xarr[px]

        if (py >= y):
            yrs = 1000000000000000000000000
            yls = yarr[y-1]
        elif (py <= 0):
            yls = -1000000000000000000000000
            yrs = yarr[0]
        else:
            yls = yarr[py-1]
            yrs = yarr[py]

        if(xls > yrs):
            px = px - 1
        elif(xrs < yls):
            px = px + 1
        
        #print(xls,xrs)
        #print(yls,yrs)
        
        #print (xls > yrs, xrs < yls)
        
        while(xls > yrs or xrs < yls):
            py = ((x + y + 1)//2) - px

            if (px >= x):
                xrs = 1000000000000000000000000
                xls = xarr[x-1]
            elif (px <= 0):
                xls = -1000000000000000000000000
                xrs = xarr[0]
            else:
                xls = xarr[px-1]
                xrs = xarr[px]

            if (py >= y):
                yrs = 1000000000000000000000000
                yls = yarr[y-1]
            elif (py <= 0):
                yls = -1000000000000000000000000
                yrs = yarr[0]
            else:
                yls = yarr[py-1]
                yrs = yarr[py]
            if(xls > yrs):
                px = px - 1
            elif(xrs < yls):
                px = px + 1
            else:
                break
        
        #print(xls,xrs)
        #print(yls,yrs)
        
        #print (xls > yrs, xrs < yls)
            
        if ((x+y)%2 == 0):
            return float((max(xls,yls) + min(xrs,yrs))/2)
        else:
            return min(max(xls,yls), min(xrs,yrs))
        
