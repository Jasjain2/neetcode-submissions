class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> seen = new HashMap<>();
        int length = nums.length;
        for(int i = 0;i<length;i++){
           int complement = target - nums[i];
            if(seen.containsKey(complement)){
                return new int[]{seen.get(complement),i};
            }
            seen.put(nums[i],i);
        }

        return new int[]{};
    }
}
