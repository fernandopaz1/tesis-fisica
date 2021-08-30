#include "../ext/googletest/googletest/include/gtest/gtest.h"
#include "../include/funciones.h"


TEST (Suma, PruebaSuma){
    EXPECT_EQ(10, sum(5,5));
    EXPECT_EQ(11, sum(12,-1));
}

TEST (Suma, PruebaSuma2){
    EXPECT_EQ(0, sum(5,-5));
    EXPECT_EQ(-8, sum(12,-20));
}